from collections import deque

n, m, V = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)


def dfs(v):
    visited_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        if arr[v][i] == 1 and visited_dfs[i] == 0:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = 1
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for i in range(1, n + 1):
            if arr[now][i] == 1 and visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = 1


dfs(V)
print()
bfs(V)
