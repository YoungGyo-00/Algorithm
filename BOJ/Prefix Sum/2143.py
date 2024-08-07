# 두 배열의 합
import bisect

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_acc = []
b_acc = []

for i in range(n):
    acc = a[i]
    a_acc.append(acc)
    for j in range(i + 1, n):
        acc += a[j]
        a_acc.append(acc)

for i in range(m):
    acc = b[i]
    b_acc.append(acc)
    for j in range(i + 1, m):
        acc += b[j]
        b_acc.append(acc)

a_acc.sort()
b_acc.sort()

answer = 0
for i in range(len(a_acc)):
    left = bisect.bisect_left(b_acc, t - a_acc[i])
    right = bisect.bisect_right(b_acc, t - a_acc[i])
    answer += right - left

print(answer)
