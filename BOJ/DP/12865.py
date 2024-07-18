# 평범한 배낭
n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# dp는 2차원 배열로 구성
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= arr[i - 1][0]:
            # 알고리즘 확인
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i - 1][0]] + arr[i - 1][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
