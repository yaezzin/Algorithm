from collections import deque

n = int(input())

orders = list(map(int, input().split()))
result = deque()
for i in range(1, n+1):
    op = orders.pop() # 연산을 거꾸로 가져옴
    
    if op == 1:
        result.appendleft(i)
    
    elif op == 2:
        result.insert(1, i) 

    elif op == 3:
        result.append(i)

print(*result)