# MooTube (Silver)
from collections import deque

N, Q = map(int, input().split())
USADO = [[] for _ in range(N + 1)]

# P(동영상 1), Q(동영상 2), R(USADO)
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    USADO[p].append((q, r))
    USADO[q].append((p, r))

# K(연관성), V(동영상 번호)
for _ in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N + 1)
    visited[v] = True
    result = 0
    queue = deque([(v, float("inf"))])

    while queue:
        v, r = queue.popleft()
        for next_v, next_r in USADO[v]:
            usado = min(r, next_r)
            if usado >= k and not visited[next_v]:
                result += 1
                queue.append((next_v, next_r))
                visited[next_v] = True
    print(result)
