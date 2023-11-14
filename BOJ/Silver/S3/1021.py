from collections import deque

n, m = map(int, input().split())
position = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

count = 0
for p in position: 
    while True:
        
        # 만약 찾으려고 하는게 맨 앞에 있으면 break
        if dq[0] == p:
            dq.popleft()
            break
        
        # 맨 앞에 없으면 계속 진행,
        else:
            # 만약 그 위치값이 중앙보다 작으면
            if dq.index(p) <= len(dq) / 2:
                # 앞에서 부터 pop해서 뒤에 넣기
                while dq[0] != p:
                    dq.append(dq.popleft())
                    count += 1

            else:
                while dq[0] != p:
                    dq.appendleft(dq.pop())
                    count += 1

print(count)