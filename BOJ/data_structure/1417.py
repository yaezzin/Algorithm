import heapq

n = int(input()) # 후보 n명
dasom = int(input()) # 다솜이의 득표수
heap = []

for _ in range(n-1):
    heapq.heappush(heap, -int(input())) # max heap으로 변경


if len(heap) == 0:
    print(0)
else:
    count = 0
    while heap:
        now = -(heapq.heappop(heap)) # 빼낼 때도 -를 붙여서 빼내야 함!!
        if now >= dasom:
            count += 1
            dasom += 1
            heapq.heappush(heap, -(now-1))
        else:
            break
    print(count)