# 가운데를 말해요
import heapq
import sys

input = sys.stdin.readline

n = int(input())
min_heap = []  # 최소 힙(오른쪽)
max_heap = []  # 최대 힙(왼쪽)

for _ in range(n):
    x = int(input())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)

    if min_heap and -max_heap[0] > min_heap[0]:
        v1 = heapq.heappop(max_heap)
        v2 = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -v2)
        heapq.heappush(min_heap, -v1)

    print(-max_heap[0])
