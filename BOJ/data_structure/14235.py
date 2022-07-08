import heapq as hq

n = int(input())

heap = []
for i in range(n):

    lst = list(map(int, input().split()))

    if lst[0] == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(-hq.heappop(heap))
    
    
    else:
        for j in range(lst[0]):
            hq.heappush(heap, -lst[j+1])
    

    