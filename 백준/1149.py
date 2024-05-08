n = int(input())
color = []
for _ in range(n):
    color.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n)]
dp[0] = color[0]

for i in range(1, n):
    # 현재 색깔 제외하고 직전 색 중 작은 값 선택
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + color[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + color[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + color[i][2]

print(min(dp[n - 1]))
