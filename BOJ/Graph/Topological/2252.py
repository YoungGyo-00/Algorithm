# 줄 세우기
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
degrees = [0] * n
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    degrees[b - 1] += 1

for i in range(n):
    if degrees[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now + 1, end=" ")
    for i in graph[now]:
        degrees[i] -= 1
        if degrees[i] == 0:
            q.append(i)
