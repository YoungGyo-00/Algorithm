# 석유 시추
from collections import deque

# 왼쪽, 위, 우측, 아래
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def solution(land):
    answer = 0

    arr = []  # 석유 위치
    size = [[] for _ in range(len(land[0]))]  # 시추관 위치마다 획득할 수 있는 덩어리
    visited = [
        [0 for _ in range(len(land[0]))] for _ in range(len(land))
    ]  # 현재 석유는 이미 확인한 것인지 판단

    # 1. 석유 위치 저장
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:
                arr.append((i, j))

    # 2. 획득 가능한 덩어리 크기 측정
    q = deque()
    for x, y in arr:
        if visited[x][y] == 1:
            continue
        temp = set()  # 석유 얻을 수 있는 위치
        s = 1  # 석유 덩어리 크기
        q.append((x, y))
        visited[x][y] = 1
        while q:
            x, y = q.pop()
            temp.add(y)
            # 네 방향을 돌면서 인접한 석유가 있는지 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 배열을 벗어난 케이스
                if nx < 0 or ny < 0 or nx >= len(land) or ny >= len(land[0]):
                    continue
                # 인접한 곳에 석유
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    q.append((nx, ny))
                    s += 1
                    visited[nx][ny] = 1
        for t in temp:
            size[t].append(s)

    for i in range(len(size)):
        answer = max(answer, sum(size[i]))

    return answer
