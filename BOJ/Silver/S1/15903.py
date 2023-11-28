import heapq

n, m = map(int, input().split())
lst = list(map(int, input().split()))

heapq.heapify(lst)

for i in range(m):

    tmp1 = heapq.heappop(lst)
    tmp2 = heapq.heappop(lst)

    new = tmp1 + tmp2

    heapq.heappush(lst, new)
    heapq.heappush(lst, new)

print(sum(lst))