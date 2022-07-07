from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split()) # n : 문서의 개수, m : 큐에서 몇번째 놓여있는지
    dq = deque(list(map(int, input().split())))
    count = 0

    while dq:
        maxValue = max(dq)
        front = dq.popleft()
        m -= 1

        if maxValue != front:
            dq.append(front)
            if m < 0:
                m = len(dq) - 1
        else:
            count += 1
            if m < 0:
                print(count)
                break

