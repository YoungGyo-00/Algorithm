# 보석 도둑
import sys, heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewelry = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewelry.sort()
bags.sort()
tmp = []
result = 0
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(tmp, -jewelry[0][1])
        heapq.heappop(jewelry)

    if tmp:
        result += heapq.heappop(tmp)
    elif not jewelry:
        break

print(-result)
