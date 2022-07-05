from collections import deque

q = deque()
n = int(input())

for i in range(1, n+1):
    q.append(i)


while len(q) > 1:
    first = q.popleft()
    second = q.popleft()
    q.append(second)

print(*q)