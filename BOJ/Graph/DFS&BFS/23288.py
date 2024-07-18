# 주사위 굴리기
from collections import deque

n, m, k = map(int, input().split())
MAP = []

for _ in range(n):
    MAP.append(list(map(int, input().split())))

# 우측, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

DICE = [1, 2, 3, 4, 5, 6]


# 점수 계산
def bfs(x, y):
    global m, n

    # 현재 숫자
    k = MAP[x][y]

    q = deque()
    q.append((x, y))

    # 다녀간 곳 확인
    map = [[0] * m for _ in range(n)]
    map[x][y] = 1

    cnt = k
    while q:
        x, y = q.popleft()
        for direction in range(4):
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != 1 and MAP[nx][ny] == k:
                cnt += k
                q.append((nx, ny))
                map[nx][ny] = 1
    return cnt


def solution():
    global m, n
    x, y, direction, ans = 0, 0, 0, 0
    for _ in range(k):
        x, y = x + dx[direction], y + dy[direction]
        # 벽에 부딪치면 반대 방향으로 이동
        if x < 0 or x > n - 1 or y < 0 or y > m - 1:
            direction = (direction + 2) % 4
            x, y = x + 2 * dx[direction], y + 2 * dy[direction]

        ans += bfs(x, y)

        # 주사위 위치 변경
        if direction == 0:
            DICE[0], DICE[2], DICE[3], DICE[5] = DICE[3], DICE[0], DICE[5], DICE[2]
        elif direction == 1:
            DICE[0], DICE[1], DICE[4], DICE[5] = DICE[1], DICE[5], DICE[0], DICE[4]
        elif direction == 2:
            DICE[0], DICE[2], DICE[3], DICE[5] = DICE[2], DICE[5], DICE[0], DICE[3]
        else:
            DICE[0], DICE[1], DICE[4], DICE[5] = DICE[4], DICE[0], DICE[5], DICE[1]

        # 방향 전환
        if DICE[5] > MAP[x][y]:
            direction = (direction + 1) % 4
        if DICE[5] < MAP[x][y]:
            direction = (direction + 3) % 4
    return ans


print(solution())
