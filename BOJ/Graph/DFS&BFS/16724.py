# 피리 부는 사나이
from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())

visited = [[-1] * m for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def move(x, y):
    if arr[x][y] == "D":
        x += 1
    elif arr[x][y] == "R":
        y += 1
    elif arr[x][y] == "U":
        x -= 1
    else:
        y -= 1
    return x, y


def isCycle(x, y, direction):
    if direction == 0 and arr[x][y] == "R":
        return True
    if direction == 1 and arr[x][y] == "D":
        return True
    if direction == 2 and arr[x][y] == "L":
        return True
    if direction == 3 and arr[x][y] == "U":
        return True
    return False


def bfs(x, y, count):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny] == -1 and isCycle(nx, ny, i):
                visited[nx][ny] = count
                q.append((nx, ny))


def solution():
    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] != -1:
                continue
            visited[i][j] = count
            x, y = i, j
            # 새로운 사이클 생성
            while True:
                bfs(x, y, count)
                dx, dy = move(x, y)
                if visited[dx][dy] != -1:
                    break
                visited[dx][dy] = count
                x, y = dx, dy
            count += 1
    return count


print(solution())
