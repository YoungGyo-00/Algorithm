# 특정한 최단 경로
import heapq

INF = 1e10
n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

# 양방향 간선
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

x, y = map(int, input().split())


def dijkstra(start):
    global n, graph
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        node, d = heapq.heappop(q)
        for next_node, next_dist in graph[node]:
            if next_dist + d < dist[next_node]:
                dist[next_node] = next_dist + d
                heapq.heappush(q, (next_node, next_dist + d))
    return dist


x_dist = dijkstra(x)
y_dist = dijkstra(y)
min_dist = min(x_dist[1] + x_dist[y] + y_dist[n], y_dist[1] + y_dist[x] + x_dist[n])

if min_dist >= INF:
    print(-1)
else:
    print(min_dist)
