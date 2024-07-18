# 구슬 탈출 2
from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(str, input())))

# 왼쪽, 위, 오른쪽, 아래 순서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 각 포인트의 위치
def find(point):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == point:
                return i, j


# 방향 별로 움직이기
def move(x, y, direction):
    nx, ny = x, y
    mv_cnt = 0

    while arr[nx][ny] != "#" and arr[nx][ny] != "O":
        nx += dx[direction]
        ny += dy[direction]
        mv_cnt += 1

    if arr[nx][ny] == "#":
        nx -= dx[direction]
        ny -= dy[direction]
        mv_cnt -= 1

    return nx, ny, mv_cnt


# bfs
def solution():
    visited = []
    r_x, r_y = find("R")
    b_x, b_y = find("B")
    visited.append((r_x, r_y, b_x, b_y))

    queue = deque()
    queue.append((r_x, r_y, b_x, b_y, 0))

    while queue:
        r_x, r_y, b_x, b_y, cnt = queue.popleft()

        if cnt > 10:
            continue

        # 왼쪽, 위, 오른쪽, 아래 순으로 실험
        for direction in range(4):
            # print(r_x, r_y, " | ", b_x, b_y)
            # print("direction :", direction)
            r_nx, r_ny, r_mv_cnt = move(r_x, r_y, direction)
            b_nx, b_ny, b_mv_cnt = move(b_x, b_y, direction)

            # print(r_nx, r_ny, " | ", b_nx, b_ny)
            # print("---------수정 후----------")

            if arr[b_nx][b_ny] == "O":
                continue

            # 만약 두 공이 같은 곳에 머물고 있으면 하나는 뒤로 가야함
            if r_nx == b_nx and r_ny == b_ny:
                if r_mv_cnt > b_mv_cnt:
                    r_nx -= dx[direction]
                    r_ny -= dy[direction]
                else:
                    b_nx -= dx[direction]
                    b_ny -= dy[direction]
            # print(r_nx, r_ny, " | ", b_nx, b_ny)

            if (r_nx, r_ny, b_nx, b_ny) in visited:
                continue

            # 해결
            if arr[r_nx][r_ny] == "O":
                return cnt + 1

            visited.append((r_nx, r_ny, b_nx, b_ny))
            queue.append((r_nx, r_ny, b_nx, b_ny, cnt + 1))

    return -1


print(solution())
