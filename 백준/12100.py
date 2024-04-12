import sys

n = int(input())

BLOCKS = []
for _ in range(n):
    BLOCKS.append([int(x) for x in sys.stdin.readline().rstrip().split()])

MAX = 0


# 왼쪽, 위, 오른쪽, 아래 순서
def move(blocks, direction):
    if direction == 1:
        for i in range(n):
            temp_idx = 0
            for j in range(1, n):
                # 0이면 Skip
                if blocks[i][j] != 0:
                    val = blocks[i][j]
                    blocks[i][j] = 0
                    # 비어 있으면 그대로 넣기
                    if blocks[i][temp_idx] == 0:
                        blocks[i][temp_idx] = val
                    # 값이 같지 않은 경우
                    elif blocks[i][temp_idx] != val:
                        temp_idx += 1
                        blocks[i][temp_idx] = val
                    # 값이 같은 경우
                    else:
                        blocks[i][temp_idx] = val * 2
                        temp_idx += 1

    if direction == 2:
        for j in range(n):
            temp_idx = 0
            for i in range(1, n):
                if blocks[i][j] != 0:
                    val = blocks[i][j]
                    blocks[i][j] = 0
                    if blocks[temp_idx][j] == 0:
                        blocks[temp_idx][j] = val
                    elif blocks[temp_idx][j] != val:
                        temp_idx += 1
                        blocks[temp_idx][j] = val
                    else:
                        blocks[temp_idx][j] = val * 2
                        temp_idx += 1

    if direction == 3:
        for i in range(n):
            temp_idx = n - 1
            for j in range(n - 1, -1, -1):
                if blocks[i][j] != 0:
                    val = blocks[i][j]
                    blocks[i][j] = 0
                    if blocks[i][temp_idx] == 0:
                        blocks[i][temp_idx] = val
                    elif blocks[i][temp_idx] != val:
                        temp_idx -= 1
                        blocks[i][temp_idx] = val
                    else:
                        blocks[i][temp_idx] = val * 2
                        temp_idx -= 1

    if direction == 4:
        for j in range(n):
            temp_idx = n - 1
            for i in range(n - 1, -1, -1):
                if blocks[i][j] != 0:
                    val = blocks[i][j]
                    blocks[i][j] = 0
                    if blocks[temp_idx][j] == 0:
                        blocks[temp_idx][j] = val
                    elif blocks[temp_idx][j] == val:
                        temp_idx -= 1
                        blocks[temp_idx][j] = val
                    else:
                        blocks[temp_idx][j] = val * 2
                        temp_idx -= 1

    return blocks


def backtracking(blocks, cnt):
    # 5번 진행했으면 바로 return
    global MAX
    if cnt == 5:
        MAX = max(MAX, max(map(max, blocks)))
        return

    # 4개의 방향으로 나눠서 진행
    for direction in range(n):
        backtracking(move(blocks, direction), cnt + 1)

    return


def solution():
    backtracking(BLOCKS, 0)
    return


solution()

print(MAX)
