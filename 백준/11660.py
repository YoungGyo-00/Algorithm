# 구간 합 구하기 5
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [0] * (n * n + 1)
for i in range(n):
    for j in range(n):
        dp[n * i + j + 1] = dp[n * i + j] + graph[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    sum = 0
    for i in range(x1, x2 + 1):
        sum += dp[n * (i - 1) + y2] - dp[n * (i - 1) + y1 - 1]
    print(sum)
