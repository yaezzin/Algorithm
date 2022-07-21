import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
adjArray = [list(map(int, input())) for _ in range(n)]
checkArray = [[False] * n for _ in range(n)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def isValidCoord(y, x):
    return 0 <= y < n and 0 <= x < n

def bfs(x, y):
    q = deque()
    q.append((x, y))
    checkArray[x][y]= True
    
    cnt = 0
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 

            if not isValidCoord(ny, nx):  
                continue
                
            if checkArray[ny][nx]:
                continue
                
            if not adjArray[ny][nx] == '0':
                continue
                
            checkArray[ny][nx] = True
            q.append((ny, nx))
            cnt += 1

    return cnt

for i in range(n):
    for j in range(n):
        if adjArray[i][j] == 1 and checkArray[i][j] == 0:
            bfs(i, j)

print(bfs(0, 0))
