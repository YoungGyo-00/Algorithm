n = int(input())
queen = [0] * n
cnt = 0


def check(row):
    for i in range(row):
        # 같은 행에 있는지 확인
        if queen[row] == queen[i]:
            return 0
        # 대각선에 퀸이 있는지 확인
        if abs(queen[row] - queen[i]) == abs(row - i):
            return 0
    # 없으면 성공
    return 1


def backtracking(start):
    global cnt

    if start == n:
        cnt += 1
        return

    for i in range(n):
        queen[start] = i
        if check(start):
            backtracking(start + 1)


backtracking(0)
print(cnt)
