from collections import deque

r, c = map(int, input().split())

arr = []
for _ in range(r):
    arr.append(list(input()))

# 북, 동, 남, 서 기준
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
pos = [(i, j) for i in range(r) for j in range(c) if arr[i][j] == "L"]  # 백조의 위치


def bfs(map):
    q = deque()
    q.append((pos[0][0], pos[0][1]))
    visited = [[0] * c for _ in range(r)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if (
                tx >= 0
                and ty >= 0
                and tx < r
                and ty < c
                and arr[tx][ty] == "."
                and not visited[tx][ty]
            ):
                q.append((tx, ty))
                visited[tx][ty] = 1
            if tx == pos[1][0] and ty == pos[1][1]:
                return 1
    return 0


def melt(arr):
    water = [(i, j) for i in range(r) for j in range(c) if arr[i][j] == "."]  # 물 위치
    while water:
        x, y = water.pop()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx >= 0 and ty >= 0 and tx < r and ty < c and arr[tx][ty] == "X":
                arr[tx][ty] = "."
    return arr


cnt = 0
while True:
    # 만날 수 있는지 검증
    if bfs(arr):
        break

    # 얼음 녹이기
    cnt += 1
    melt(arr)

print(cnt)
