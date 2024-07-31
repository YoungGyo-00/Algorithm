# 팰린드롭?
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
questions = []

for _ in range(m):
    questions.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1
    else:
        dp[i][i + 1] = 0

# 3 이상
for cnt in range(n - 2):
    for i in range(n - 2 - cnt):
        j = i + cnt + 2  # 양 끝 i, j
        if arr[i] == arr[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

for start, end in questions:
    print(dp[start - 1][end - 1])
