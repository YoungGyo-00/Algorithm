n = int(input())
arr = list(map(int, input().split()))

dp_left = [1] * n
dp_right = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)

for i in range(n - 2, -1, -1):
    for j in range(n - 1, i - 1, -1):
        if arr[j] < arr[i]:
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)

for i in range(n):
    dp_left[i] += dp_right[i]

print(max(dp_left) - 1)
