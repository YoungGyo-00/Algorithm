# ACM Craft
from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    inDegree = [0 for _ in range(n)]
    dp = [0 for _ in range(n)]
    q = deque()

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        inDegree[b - 1] += 1

    w = int(input())
    for i in range(n):
        if inDegree[i] == 0:
            dp[i] = d[i]
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            inDegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + d[i])
            if inDegree[i] == 0:
                q.append(i)

    print(dp[w - 1])
