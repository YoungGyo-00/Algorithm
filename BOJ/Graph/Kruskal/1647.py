# 도시 분할 계획
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()
parent = [i for i in range(n + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


answer = 0
last = 0
for i in range(m):
    c, a, b = graph[i]
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += c
        last = c

print(answer - last)
