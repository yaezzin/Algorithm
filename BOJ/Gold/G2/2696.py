import heapq
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    lst_count = int(input()) # 수열의 크기
    
    lst = []
    if lst_count % 10 == 0:
        for _ in range(lst_count//10):
            lst.extend(list(map(int, input().split())))
    else:
        for _ in range(lst_count//10+1):
            lst.extend(list(map(int, input().split())))

    left_heap = [] # 최대힙
    right_heap = [] # 최소힙
    answer = []
    count = 1

    for i in lst:
        # 만약 동일한 크기만 큼 들어있다면 최대힙에 넣음
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -i)
        
        # 그렇지 않으면 최소힙에 넣음
        else:
            heapq.heappush(right_heap, i)
        
        # 만약 최소 힙에 있는 것이 최대 힙보다 크면 바꿔줘야함!
        if right_heap and right_heap[0] < -left_heap[0]:
            left_value = heapq.heappop(left_heap)
            right_value = heapq.heappop(right_heap)

            heapq.heappush(left_heap, -right_value)
            heapq.heappush(right_heap, -left_value)

        if count % 2 != 0:
            answer.append(-left_heap[0])
        count += 1
        
    print(len(answer))
    for i in range(len(answer)):
        if i != 0 and (i+1) % 10 == 1:
            print()
        print(answer[i], end=' ')