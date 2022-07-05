from collections import deque

n = int(input())
dq = deque()
dq.append(n)

for i in range(n-1, 0, -1):
    dq.appendleft(i)

    for j in range(i):
        last = dq.pop()
        dq.appendleft(last)

print(*dq)