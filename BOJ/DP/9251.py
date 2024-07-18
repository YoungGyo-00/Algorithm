# LCS
arr_1 = list(input())
arr_2 = list(input())

lcs = [[0] * (len(arr_2) + 1) for _ in range(len(arr_1) + 1)]

for i in range(1, len(arr_1) + 1):
    for j in range(1, len(arr_2) + 1):
        if arr_1[i - 1] == arr_2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(lcs[-1][-1])
