from collections import deque

K = int(input())
w, h = map(int, input().split())

board = [input().split() for _ in range(h)]

checkArray = [[[False] * (K + 1) for _ in range(w)] for _ in range(h)]

dy = [0, 1, 0, -1, 1, 2, 2, 1, -1, -2, -2 ,- 1]
dx = [1, 0, -1, 0, 2, 1, -1, -2, -2, -1 ,1 ,-2]
dk = [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1]

checkArray[0][0][K] = True
q = deque()
q.append((0, 0, K, 0))

def isValidCoord(y, x, k):
    return 0<= y < h and 0 <= x < w and 0 <= k <= K

while q:
    y, x, k, d = q.popleft()

    if y == h - 1 and x == w - 1:
        print(d)
        exit(0)

    for i in range(12):
        
        ny = y + dy[i]
        nx = x + dx[i]
        nk = k + dk[i]
        nd = d + 1
        
        if not isValidCoord(ny, nx, nk):
            continue

        if checkArray[ny][nx][nk]:
            continue

        if board[ny][nx] == "1":
            continue

        checkArray[ny][nx][nk] = True
        q.append((ny, nx, nk, nd))


print(-1)  


