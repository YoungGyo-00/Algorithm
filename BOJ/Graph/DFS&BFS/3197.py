# 백조의 호수
from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())

arr = []
for _ in range(r):
    arr.append(list(input()))

# 북, 동, 남, 서 기준
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
pos = [(i, j) for i in range(r) for j in range(c) if arr[i][j] == "L"]  # 백조의 위치


def bfs(arr):
    q = deque()
    q.append((pos[0][0], pos[0][1]))
    visited = [[0] * c for _ in range(r)]
    visited[pos[0][0]][pos[0][1]] = 1
    while q:
        x, y = q.popleft()
        if x == pos[1][0] and y == pos[1][1]:
            return 1
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < r and 0 <= ty < c and not visited[tx][ty]:
                if arr[tx][ty] == "X":
                    arr[tx][ty] = "."
                else:
                    q.append((tx, ty))
                visited[tx][ty] = 1
    return 0


def melt(arr):
    q = deque()
    q.append((pos[1][0], pos[1][1]))
    visited = [[0] * c for _ in range(r)]
    visited[pos[1][0]][pos[1][1]] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < r and 0 <= ty < c and not visited[tx][ty]:
                if arr[tx][ty] == ".":
                    q.append((tx, ty))
                if arr[tx][ty] == "X":
                    arr[tx][ty] = "."
                visited[tx][ty] = 1
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
