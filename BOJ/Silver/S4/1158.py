from collections import deque

n, k = map(int, input().split())
q = deque(i for i in range(1, n+1))

result = deque()
i = 1
while q:
    if i % k == 0:
        result.append(q.popleft())
    else:
        q.append(q.popleft())
    
    i += 1


answer = "<" + ', '.join(map(str, result)) + ">"
print(answer)