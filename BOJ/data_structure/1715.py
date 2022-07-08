import heapq as hq

n = int(input())
heap = []

for i in range(n):
    hq.heappush(heap, int(input()))

if len(heap) == 1:
    print(0)

else:
    count = 0
    while len(heap) > 1:
        tmp1 = hq.heappop(heap)
        tmp2 = hq.heappop(heap)
        count += (tmp1 + tmp2)
        hq.heappush(heap, tmp1 + tmp2)

print(count)


