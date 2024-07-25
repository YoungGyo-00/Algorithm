# 부분합
n, s = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [[0] for _ in range(n)]
prefix_sum[0] = arr[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

left = 0
right = 0

while prefix_sum[right] < s:
    right += 1
    if right == n:
        break

# 맨 처음 길이 측정
length = right + 1

# 부분합 구하기
while right < n:
    if length == 1:
        break

    if prefix_sum[right] - prefix_sum[left] >= s:
        length = min(right - left, length)
        left += 1
    else:
        right += 1

if prefix_sum[n - 1] < s:
    print(0)
else:
    print(length)
