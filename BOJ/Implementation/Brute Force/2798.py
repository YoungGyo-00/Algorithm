n, m = map(int, input().split())
lst = list(map(int, input().split()))
nlst = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            three = lst[i] + lst[j] + lst[k]
            if three > m:
                continue
            else:
                nlst.append(three)
print(max(nlst))
