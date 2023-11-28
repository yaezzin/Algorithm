import heapq

n = int(input())
plus_heap = []
minus_heap = []
one = []
zero = []

for _ in range(n):
    i = int(input())

    if i > 1:
        heapq.heappush(plus_heap, (-i, i))
    
    elif i == 1:
        heapq.heappush(one, i)

    elif i == 0:
        heapq.heappush(zero, i)
    
    else:
        heapq.heappush(minus_heap, i)

answer = []

# 양수는 큰거끼리 묶어서 곱하기
while len(plus_heap) > 1:
    tmp1 = heapq.heappop(plus_heap)[1]
    tmp2 = heapq.heappop(plus_heap)[1]
    result = tmp1 * tmp2
    answer.append(result)

# 만약 남아 있으면 정답에 그냥 넣기
if len(plus_heap) != 0:
    answer.append(heapq.heappop(plus_heap)[1])

# 음수도 모아서 곱하기
while len(minus_heap) > 1:
    tmp1 = heapq.heappop(minus_heap)
    tmp2 = heapq.heappop(minus_heap)
    result = tmp1 * tmp2
    answer.append(result)

# 음수가 남았다면 0이랑 곱해줄 것임
# 따라서, 음수가 남았고, 0이 없으면 그냥 음수 넣어주기
if len(minus_heap) !=0 and len(zero) == 0:
    answer.append(heapq.heappop(minus_heap))

# 1이 남았다면 그냥 넣어주기
while len(one) !=0:
    answer.append(heapq.heappop(one))

print(sum(answer))
