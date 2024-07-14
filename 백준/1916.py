# 최소비용 구하기
import heapq
import sys

input = sys.stdin.readline

INF = 1e10

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        node, d = heapq.heappop(q)
        if dist[node] < d:
            continue
        for next_node, c in graph[node]:
            if d + c < dist[next_node]:
                dist[next_node] = d + c
                heapq.heappush(q, (next_node, d + c))
    return dist


start, end = map(int, input().split())
dist = dijkstra(start)
print(dist[end])
