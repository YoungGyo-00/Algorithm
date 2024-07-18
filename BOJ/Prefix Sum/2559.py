n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 누적 합 구하기
acc = []
temp = 0
for i in range(n):
    temp += arr[i]
    acc.append(temp)

# 구간 합 구하기
max = acc[k - 1]
for i in range(1, n - k + 1):
    now = acc[i + k - 1] - acc[i - 1]
    if max < now:
        max = now

print(max)
