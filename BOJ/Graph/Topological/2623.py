# 음악프로그램
from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
depth = [0] * n

for _ in range(m):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp) - 1):
        arr[temp[i] - 1].append(temp[i + 1] - 1)
        depth[temp[i + 1] - 1] += 1

q = deque()

for i in range(n):
    if depth[i] == 0:
        q.append(i)

answer = []
while q:
    now = q.popleft()
    answer.append(now)
    for num in arr[now]:
        depth[num] -= 1
        if depth[num] == 0:
            q.append(num)

if len(answer) != n:
    print(0)
else:
    for num in answer:
        print(num + 1)
