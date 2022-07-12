from collections import deque

n, m = map(int, input().split())
board = [input() for _ in range(n)]
print(board)
checkArray = [[False] * m for _ in range(n)]
print(checkArray)

q = deque()
q.append((0, 0, 1))
checkArray[0][0] = True

def isValidCoord(y, x):
    return 0 <= y < n and 0 <= x < m

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

while q:
    y, x, d = q.popleft()
    
    if y == n-1 and x == m-1:
        print(d)
        break

    for i in range(4):
        ny = y + dy[i]  # next y, x
        nx = x + dx[i]
        nd = d + 1
        
        if not isValidCoord(ny, nx):
            continue
        if checkArray[ny][nx]:
            continue
        if board[ny][nx] == '0':
            continue
        
        checkArray[ny][nx] = True
        q.append((ny, nx, nd))
