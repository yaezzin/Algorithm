from collections import deque
import sys

n = int(input())
dq = deque(enumerate(map(int, sys.stdin.readline().split())))
lst = []


while dq:
    index, tmp = dq.popleft()
    lst.append(index+1)

    if tmp > 0:
        dq.rotate(-(tmp-1))
    else:
        dq.rotate(-tmp)

for i in lst:
    print(i, end = " ")