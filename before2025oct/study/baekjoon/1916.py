from sys import stdin
import heapq

# 다익스트라 알고리즘


def dijkstra(graph, start):
    dis = [int(1e9)] * (N + 1)
    dis[start] = 0
    queue = []
    heapq.heappush(queue, [dis[start], start])

    while queue:
        dist, node = heapq.heappop(queue)
        if dis[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < dis[next_node]:  #
                dis[next_node] = distance
                heapq.heappush(queue, [distance, next_node])

    return dis


input = stdin.readline

N = int(input())
M = int(input())

# make city node
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    # [[]]
    graph[a].append([b, cost])

start, end = map(int, input().split())


dis_start = dijkstra(graph, start)
print(dis_start[end])
