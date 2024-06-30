# 트리의 지름
from collections import deque

v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    l = list(map(int, input().split()))
    index = 1
    while l[index] != -1:
        node, cost = l[index], l[index + 1]
        graph[l[0]].append((node, cost))
        index += 2


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [-1] * (v + 1)
    visited[start] = 0
    res = [0, 0]

    while q:
        node, cost = q.popleft()
        for next_node, next_cost in graph[node]:
            if visited[next_node] == -1:
                cal = cost + next_cost
                q.append((next_node, cal))
                visited[next_node] = cal
                if res[1] < cal:
                    res[0] = next_node
                    res[1] = cal
    return res


point, _ = bfs(1)
print(bfs(point)[1])
