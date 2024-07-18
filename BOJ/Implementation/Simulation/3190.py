# 뱀
from collections import deque

n = int(input())
k = int(input())

apple = []
for _ in range(k):
    apple.append(list(map(int, input().split())))

l = int(input())
direction_info = dict()
for _ in range(l):
    x, c = input().split()
    direction_info[int(x)] = c

# 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move(x, y, direction):
    nx = x + dx[direction]
    ny = y + dy[direction]

    return nx, ny


# 게임 종료
def check(snake, x, y):
    # 벽에 부딪치는 경우
    if x == 0 or y == 0 or x == n + 1 or y == n + 1:
        return 1

    # 뱀 몸통에 부딪치는 경우
    if (x, y) in snake:
        return 1
    return 0


def solution():
    # 뱀의 머리
    nx, ny = 1, 1
    # 뱀의 몸통
    body = deque()
    body.append((1, 1))
    # 시간, 방향
    cnt = 0
    direction = 0

    while True:
        # 방향 설정
        if cnt in direction_info:
            if direction_info[cnt] == "D":
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4

        # 뱀의 머리
        x, y = nx, ny
        nx, ny = move(x, y, direction)
        cnt += 1

        # 게임 종료 체크
        if check(body, nx, ny):
            break

        # 사과 위치 체크
        if [nx, ny] not in apple:
            body.popleft()
        body.append((nx, ny))
    return cnt


print(solution())
