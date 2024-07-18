n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

count_0 = 0
count_1 = 0


def solution(row, column, length):
    temp = arr[row][column]
    for i in range(row, row + length):
        for j in range(column, column + length):
            if temp != arr[i][j]:
                solution(row, column, length // 2)
                solution(row, column + length // 2, length // 2)
                solution(row + length // 2, column, length // 2)
                solution(row + length // 2, column + length // 2, length // 2)
                return
    if temp == 0:
        global count_0
        count_0 += 1
    else:
        global count_1
        count_1 += 1


solution(0, 0, n)
print(count_0)
print(count_1)
