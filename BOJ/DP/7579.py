# 앱
import copy

n, m = map(int, input().split())
a_arr = list(map(int, input().split()))
c_arr = list(map(int, input().split()))

dp = [[0 for _ in range(n * 100 + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    # 1. 일단 자기 cost 에 있는 값과 비교해서 크면 교체
    dp[i] = copy.deepcopy(dp[i - 1])
    dp[i][c_arr[i - 1]] = max(a_arr[i - 1], dp[i - 1][c_arr[i - 1]])
    for j in range(c_arr[i - 1] + 1, 100 - c_arr[i - 1]):
        # 2. 이후 자기 cost를 앞에 있는 값과 비교해서 크면 교체
        dp[i][j] = max(dp[i - 1][j - c_arr[i - 1]] + a_arr[i - 1], dp[i - 1][j])

    print(dp[i][:15])

for i in range(n * 100 + 1):
    if dp[n][i] >= m:
        print(i)
        break
