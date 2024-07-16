# 트리와 쿼리
import sys

sys.setrecursionlimit(1000000000)

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent_arr = [-1] * (n + 1)
child = [[] for _ in range(n + 1)]


def makeTree(currentNode, parent):
    for nextNode in graph[currentNode]:
        if nextNode != parent:
            child[currentNode].append(nextNode)
            parent_arr[nextNode] = currentNode
            makeTree(nextNode, currentNode)


size = [0] * (n + 1)


def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for node in child[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]


makeTree(r, -1)
countSubtreeNodes(r)

for _ in range(q):
    num = int(input())
    print(size[num])
