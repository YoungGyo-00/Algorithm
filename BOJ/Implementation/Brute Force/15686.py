# 치킨 배달
from itertools import combinations


def cal(arr1, arr2):
    dx = abs(arr1[0] - arr2[0])
    dy = abs(arr1[1] - arr2[1])
    return dx + dy


n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))
        if arr[i][j] == 1:
            house.append((i, j))

ans = 1e12
for chi in combinations(chicken, m):
    dist = 0
    for l in house:
        d = 999
        for j in range(m):
            d = min(d, abs(l[0] - chi[j][0]) + abs(l[1] - chi[j][1]))
        dist += d
    if dist < ans:
        ans = dist

print(ans)
