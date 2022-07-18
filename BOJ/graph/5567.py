# 1번 정점에서 거리가 2이하인 정점을 모두 카운트
from collections import deque

n = int(input())
m = int(input())

adjArray = [[False] * n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    adjArray[a][b] = True
    adjArray[b][a] = True
    
checkArray = [False] * n

def bfs(startNode):
    checkArray[startNode] = True
    q = deque()

    q.append((startNode, 0))

    count = 0
    while q:
        count += 1
        currentNode, distance = q.popleft()

        if distance == 2:
            continue

        for nextNode in range(n):
            if not adjArray[currentNode][nextNode]:
                continue
            if checkArray[nextNode]:
                continue

            checkArray[nextNode] = True
            q.append((nextNode, distance +1))
    
    return count - 1

print(bfs(0))