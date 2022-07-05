import heapq as h

n, m = map(int, input().split())
giftArray = list(map(int, input().split()))
wishArray = list(map(int, input().split()))
heap = []

for i in giftArray:
    h.heappush(heap, -i)

for w in wishArray:
    pop = -h.heappop(heap)

    if pop > w:
        h.heappush(heap, -(pop - w))

    elif pop == w:
        continue

    else:
        print(0)
        exit()

print(1)
