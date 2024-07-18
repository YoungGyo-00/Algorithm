# 인간-컴퓨터 상호작용
import sys

input = sys.stdin.readline

arr = input().rstrip()
n = int(input())

dp = [[0] * 26]

for i in range(len(arr)):
    alpha = ord(arr[i]) - ord("a")
    dp.append(dp[-1][:])
    dp[i + 1][alpha] += 1

for _ in range(n):
    alpha, start, end = input().split()
    alpha = ord(alpha) - ord("a")
    start, end = int(start), int(end)
    print(dp[end + 1][alpha] - dp[start][alpha])
