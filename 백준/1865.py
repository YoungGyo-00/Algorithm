# 웜홀(그래프 이론)
INF = 1e10

tc = int(input())


def bellman(graph, start, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    for i in range(n + 1):
        for road in graph:
            s, e, t = road
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                # 음의 순환 사이클이 있는지 확인
                if i == n:
                    return 1
    return 0


for _ in range(tc):
    # n(지점의 수), m(도로의 개수), 웜홀의 개수(w)
    n, m, w = map(int, input().split())
    graph = []

    # 양방향 도로
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    # 단방향 웜홀
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))

    if bellman(graph, 1, n):
        print("YES")
    else:
        print("NO")
