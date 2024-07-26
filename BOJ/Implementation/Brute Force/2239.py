# 스도쿠

arr = []
idx = []
answer = []
flag = 0

for i in range(9):
    number = list(map(int, input()))
    arr.append(number)
    for j in range(9):
        if number[j] == 0:
            idx.append((i, j))

length = len(idx)


def check_row(c, num):
    for i in range(9):
        if arr[i][c] == num:
            return 0
    return 1


def check_column(r, num):
    for i in range(9):
        if arr[r][i] == num:
            return 0
    return 1


def check_box(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for x in range(3):
        for y in range(3):
            if arr[nr + x][nc + y] == num:
                return 0
    return 1


def solution(i):
    global flag
    if length == i:
        flag = 1
        return

    r, c = idx[i]
    for num in range(1, 10):
        if check_column(r, num) and check_row(c, num) and check_box(r, c, num):
            arr[r][c] = num
            solution(i + 1)
            if flag == 1:
                return
            arr[r][c] = 0


solution(0)
for i in range(9):
    print("".join(map(str, arr[i])))
