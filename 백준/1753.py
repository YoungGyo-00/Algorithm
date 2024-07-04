# 최단경로(그래프 이론)
import heapq
import sys

INF = int(1e10)
input = sys.stdin.readline

V, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(graph, start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        node, d = heapq.heappop(q)
        if dist[node] < d:
            continue
        for next_node, c in graph[node]:
            if dist[next_node] > d + c:
                dist[next_node] = d + c
                heapq.heappush(q, (next_node, d + c))
    return dist


dist = dijkstra(graph, start)
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
        continue
    print(dist[i])
