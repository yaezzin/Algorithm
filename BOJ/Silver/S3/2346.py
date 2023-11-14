from collections import deque

n = int(input())
lst = list(map(int, input().split()))
queue = deque((i+1, lst[i]) for i in range(len(lst))) # (index, value)

result = []
while queue:
    num = queue.popleft() # (1, 3)
    result.append(num[0]) 

    if len(queue) == 0:
        break

    # 만약 뽑은 숫자가 양수이면
    if num[1] > 0:
        for i in range(num[1]-1):
            queue.append(queue.popleft())
    
    # 뽑은 숫자가 음수이면
    else:
        for i in range(abs(num[1])):
            queue.appendleft(queue.pop())
    



print(*result)

    
                       
    
        