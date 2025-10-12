#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re
import sys
import time
import requests
from typing import Any, Dict, Optional

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    print("환경변수 OPENAI_API_KEY가 없습니다.", file=sys.stderr)
    sys.exit(1)

URL = "https://api.openai.com/v1/responses"
MODEL = "o4-mini-deep-research-2025-06-26"

DEFAULT_QUESTION = (
    "암 환자를 위한 대처 가이드를 한국어 JSON으로 반환하라. "
    "키는 overview, immediate_actions, treatment, side_effects, lifestyle, mental_support, korea_resources, sources. "
    "각 키는 배열 또는 객체로 채우고, 모든 텍스트는 한국어. URL은 절대경로. "
    "반드시 유효한 JSON만 출력하고 코드블록이나 추가 설명은 금지한다. "
    "출처는 대한민국 공공기관/대학병원/WHO/NCI 등 공신력 높은 기관을 우선하고, 최소 5개 이상 제시하라. "
    "이 응답은 의학적 조언이 아니라 정보 제공 목적임을 overview 첫 문장에 명시하라."
)

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# -------- Retry helpers --------
RETRY_STATUS = {429, 500, 502, 503, 504}


def _post_with_retry(
    url: str, json_body: Dict[str, Any], retries: int = 5, base_delay: float = 1.5
) -> requests.Response:
    for i in range(retries):
        resp = requests.post(url, headers=HEADERS, json=json_body, timeout=(20, 90))
        if resp.status_code < 400 or resp.status_code not in RETRY_STATUS:
            return resp
        time.sleep(base_delay * (2**i))
    return resp  # 마지막 응답 반환


def _get_with_retry(
    url: str, retries: int = 5, base_delay: float = 1.5
) -> requests.Response:
    for i in range(retries):
        resp = requests.get(url, headers=HEADERS, timeout=(20, 90))
        if resp.status_code < 400 or resp.status_code not in RETRY_STATUS:
            return resp
        time.sleep(base_delay * (2**i))
    return resp  # 마지막 응답 반환


# -------- Deep Research flow --------
def build_payload(question: str) -> Dict[str, Any]:
    return {
        "model": MODEL,
        "input": question,
        "text": {"format": {"type": "json_object"}},
        "tools": [
            {
                "type": "web_search_preview",
                "search_context_size": "medium",
            }
        ],
        "background": True,
    }


def start_background(question: str) -> str:
    payload = build_payload(question)
    resp = _post_with_retry(URL, payload)
    if resp.status_code >= 400:
        raise RuntimeError(f"HTTP {resp.status_code}: {resp.text}")
    data = resp.json()
    if "id" not in data:
        raise RuntimeError(f"응답에 id가 없습니다: {data}")
    return data["id"]


def retrieve(resp_id: str) -> Dict[str, Any]:
    resp = _get_with_retry(f"{URL}/{resp_id}")
    if resp.status_code >= 400:
        raise RuntimeError(f"HTTP {resp.status_code}: {resp.text}")
    return resp.json()


def run_background_then_poll(
    question: str, interval: int = 8, max_wait: int = 1200
) -> Dict[str, Any]:
    resp_id = start_background(question)
    waited = 0
    print(f"[INFO] Background job started: {resp_id}", file=sys.stderr)
    while waited < max_wait:
        time.sleep(interval)
        waited += interval
        rj = retrieve(resp_id)
        status = rj.get("status")
        print(f"[INFO] Status: {status} (waited {waited}s)", file=sys.stderr)
        if status in {"completed", "succeeded", "success"}:
            return rj
        if status in {"failed", "cancelled", "canceled", "errored"}:
            raise RuntimeError(
                f"Deep research failed: {json.dumps(rj, ensure_ascii=False)}"
            )
        # 상태가 queued/in_progress 등인 경우 계속 대기
    raise TimeoutError("Deep research polling timed out")


# -------- Parsing helpers --------
def extract_output_text(rj: Dict[str, Any]) -> Optional[str]:
    # 1) 편의 필드
    out = rj.get("output_text")
    if out:
        return out

    # 2) 메시지 배열에서 찾기
    output = rj.get("output", [])
    if isinstance(output, list):
        for item in output:
            if item.get("type") == "message":
                for c in item.get("content", []):
                    if c.get("type") == "output_text" and c.get("text"):
                        return c["text"]

    # 3) tool / reasoning 등 기타 경로가 있을 수 있으나 일반적이지 않음
    return None


def try_json_parse(text: Optional[str]) -> Optional[Dict[str, Any]]:
    if not text:
        return None
    # 우선 그대로 시도
    try:
        return json.loads(text)
    except Exception:
        pass
    # 느슨한 추출(가장 바깥 {})
    m = re.search(r"\{.*\}\s*$", text, flags=re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except Exception:
            return None
    return None


# -------- Main --------
def main():
    question = " ".join(sys.argv[1:]).strip() or DEFAULT_QUESTION
    try:
        rj = run_background_then_poll(question, interval=8, max_wait=1200)
        text = extract_output_text(rj)
        data = try_json_parse(text)
        if data is None:
            # JSON 파싱 실패시, 원문 텍스트 또는 전체 응답 출력
            if text:
                print(text)
            else:
                print(json.dumps(rj, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(data, ensure_ascii=False, indent=2))
    except Exception as e:
        # 오류 상황을 JSON으로 표준화해 출력(파이프라인에서 다루기 좋게)
        err = {
            "error": True,
            "message": str(e),
            "type": e.__class__.__name__,
        }
        print(json.dumps(err, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
