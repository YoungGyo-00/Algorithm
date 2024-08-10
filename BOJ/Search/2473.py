# 세 용액
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

num = 1e11
ans_l = 1
ans_r = len(arr) - 1
fixed = 0
for i in range(len(arr) - 1):
    left = i + 1
    right = len(arr) - 1
    while left < right:
        temp = arr[i] + arr[left] + arr[right]
        if abs(temp) < num:
            fixed = i
            num = abs(temp)
            ans_l = left
            ans_r = right
        if temp < 0:
            left += 1
        else:
            right -= 1

print(arr[fixed], arr[ans_l], arr[ans_r])
