import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    # 0 : 제거 후 출력
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-num, num))