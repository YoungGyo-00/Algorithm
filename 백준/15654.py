# N과 M(5)
n, m = map(int, input().split())
dictionary = list(map(int, input().split()))
dictionary.sort()
l = []


def dfs():
    if len(l) == m:
        print(" ".join(map(str, l)))
        return
    for i in range(0, n):
        if dictionary[i] not in l:
            l.append(dictionary[i])
            dfs()
            l.pop()


dfs()
