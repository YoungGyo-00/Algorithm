n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0]
tmp = 0

# 누적 합 구하기
for i in arr:
    tmp = tmp + i
    sum.append(tmp)

# 구간 합 구하기
for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i - 1])
