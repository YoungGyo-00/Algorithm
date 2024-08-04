# 사이클 게임
n, m = map(int, input().split())
parent = [i for i in range(n)]


def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a > parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a


flag = 0
num = 1
for _ in range(m):
    a, b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        flag = 1
        break

    union(a, b)
    num += 1

if flag:
    print(num)
else:
    print(0)
