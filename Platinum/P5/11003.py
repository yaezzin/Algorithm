import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    # 1. 덱의 마지막 위치부터 현재 값보다 큰 값은 덱에서 제거
    while mydeque and now[i] < mydeque[-1][0]:
        mydeque.pop()
    # 2.덱의 마지막에 (현재값, 인덱스) 저장
    mydeque.append((now[i], i))

    # 3. L 범위(슬라이딩윈도우)를 넘어가는 값은 삭제 (index - L <= index)
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    # 4. 출력
    print(mydeque[0][0], end=' ')