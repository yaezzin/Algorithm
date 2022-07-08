import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()

for i in range(n):
    word = input().split()
    order = word[0]

    if order == 'push_front':
        dq.appendleft(word[1])

    elif order == 'push_back':
        dq.append(word[1])

    elif order == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
        
    elif order == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    elif order == 'size':
        print(len(dq))

    elif order == 'empty':
        if len(dq) == 0:
            print(1)
        print(0)

    elif order == 'front':
        if len(dq) == 0:
            print(-1)
        print(dq[0])

    elif order == 'back':
        if len(dq) == 0:
            print(-1)
        print(dq[-1])
            
