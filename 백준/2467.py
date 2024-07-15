# 용액
n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

ans_left = 0
ans_right = n - 1
ans = abs(arr[left] + arr[right])

while left < right:
    if abs(arr[left] + arr[right]) < ans:
        ans = abs(arr[left] + arr[right])
        ans_left = left
        ans_right = right

    if ans == 0:
        break

    if arr[left] + arr[right] < 0:
        left += 1
    else:
        right -= 1

print(arr[ans_left], arr[ans_right])
