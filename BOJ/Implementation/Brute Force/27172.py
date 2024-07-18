# 수 나누기 게임
import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
s = set(cards)
m = max(cards)
scores = [0] * (m + 1)

for i in cards:
    for j in range(2 * i, m + 1, i):
        if j in s:
            scores[i] += 1
            scores[j] -= 1

for i in cards:
    print(scores[i], end=" ")
