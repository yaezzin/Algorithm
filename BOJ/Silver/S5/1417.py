import heapq
import sys
input = sys.stdin.readline

n = int(input())
my_num = int(input())

heap = []
for i in range(n-1):
    num = int(input())
    heapq.heappush(heap, (-num, num))

count = 0

while heap:
    tuple = heapq.heappop(heap)
    max = tuple[1]

    if my_num <= max:
        my_num += 1
        max -= 1
        count += 1
        heapq.heappush(heap, (-max, max))
    

print(count)
