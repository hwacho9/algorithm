cnt = 0


def dfs(numbers, target, idx, result):
    global cnt
    if idx == len(numbers):
        if result == target:
            cnt += 1
            return
    else:
        dfs(numbers, target, idx + 1, result + numbers[idx])
        dfs(numbers, target, idx + 1, result - numbers[idx])


def solution(numbers, target):
    answer = 0

    dfs(numbers, target, 0, answer)
    return cnt


# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
# https://jyeonnyang2.tistory.com/242
