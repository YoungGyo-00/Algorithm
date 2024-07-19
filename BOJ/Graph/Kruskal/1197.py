# 최소 스패닝 트리
v, e = map(int, input().split())
edges = []
parent = [i for i in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])
answer = 0


# 부모가 자기가 아닐 경우
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a < parent_b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(e):
    a, b, c = edges[i]
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += c

print(answer)
