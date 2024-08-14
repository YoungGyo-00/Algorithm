# 체스판 다시 칠하기
n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(input())

min = 100000


def solution(row, column, color):
    check = (row + column) % 2
    count = 0
    for i in range(row, row + 8):
        for j in range(column, column + 8):
            if (i + j) % 2 == check and color != board[i][j]:
                count += 1
            if (i + j) % 2 != check and color == board[i][j]:
                count += 1
    return count


for i in range(n - 7):
    for j in range(m - 7):
        count_w = solution(i, j, "W")
        count_b = solution(i, j, "B")
        if min > count_w:
            min = count_w
        if min > count_b:
            min = count_b

print(min)
