import sys  # 非常に大きな数を使うために sys.maxsize を使用

# グラフの定義：各ノードからつながるノードとコストのリスト
graph = {1: [(2, 2), (3, 5)], 2: [(3, 1), (4, 2)], 3: [(4, 3)], 4: []}

# 最短距離テーブルの初期化：すべて無限大にして、スタートノード（1）は0に設定
dist = {node: sys.maxsize for node in graph}
dist[1] = 0  # スタート地点までの距離は0

visited = set()  # 訪問済みノードを記録するセット

# 全てのノードを訪問するまで繰り返す
while len(visited) < len(graph):
    min_node = None
    # 未訪問ノードの中から最も距離が短いノードを探す
    # 매번 모든 노드 확인해서 최소 거리 노드를 직접 찾음
    for node in graph:
        if node not in visited and (min_node is None or dist[node] < dist[min_node]):
            min_node = node

    visited.add(min_node)  # 選ばれたノードを訪問済みにする

    # 選ばれたノードに隣接するノードの距離を更新
    for neighbor, cost in graph[min_node]:
        # より短い経路が見つかれば更新する
        if dist[min_node] + cost < dist[neighbor]:
            dist[neighbor] = dist[min_node] + cost

# 各ノードまでの最短距離を出力
print(dist)
