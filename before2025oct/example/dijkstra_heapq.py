import heapq  # ヒープ（優先度付きキュー）を使うためにインポート

# グラフの定義：各ノードからの接続先とコストのリスト
graph = {1: [(2, 2), (3, 5)], 2: [(3, 1), (4, 2)], 3: [(4, 3)], 4: []}

# 最短距離テーブルの初期化：すべて無限大（inf）、スタートノード(1)は0
dist = {node: float("inf") for node in graph}
dist[1] = 0  # スタートノードの距離を0に設定

# 優先度付きキュー（距離, ノード）でスタートノードを追加
queue = [(0, 1)]

# キューが空になるまで繰り返し処理
while queue:
    cur_dist, node = heapq.heappop(queue)  # 最も距離が小さいノードを取り出す

    # すでにより短い距離で訪問済みならスキップ
    if cur_dist > dist[node]:
        continue

    # 隣接ノードを確認し、距離が短くなる場合は更新
    for neighbor, cost in graph[node]:
        new_dist = cur_dist + cost
        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(
                queue, (new_dist, neighbor)
            )  # 更新されたノードをキューに追加

# 結果を出力：各ノードまでの最短距離
print(dist)


def unique(elements):
    temp = {}
    for element in elements:
        temp[element] = None
    return temp.keys()


unique_elements = unique([1, 2, 2])


unique_elements = set([1, 2, 2])
