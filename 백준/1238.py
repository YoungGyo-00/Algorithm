# 1238 파티
import heapq

INF = 1e10

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    reverse_graph[b].append((a, c))


def dijkstra(start, edge):
    dist = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        next_node, cost = heapq.heappop(q)
        if dist[next_node] < cost:
            continue
        for next, c in edge[next_node]:
            if dist[next] > cost + c:
                heapq.heappush(q, (next, cost + c))
                dist[next] = cost + c

    return dist


node2x = dijkstra(x, reverse_graph)
x2node = dijkstra(x, graph)

print(max([x2node[i] + node2x[i] for i in range(1, n + 1) if i != x]))
