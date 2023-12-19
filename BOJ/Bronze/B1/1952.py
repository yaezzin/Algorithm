m, n = map(int, input().split())
lst = [[0] * n for _ in range(m)]
lst[0][0] = 1

def in_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

def solution():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cur = 0
    cnt = 0
    x, y = 0, 0
    for _ in range(2, n * m + 1):

        nx = x + dx[cur]
        ny = y + dy[cur]

        if not in_range(nx, ny) or lst[nx][ny] != 0:
            cur = (cur + 1) % 4
            cnt += 1
        
        x = x + dx[cur]
        y = y + dy[cur]

        lst[x][y] = 1
    
    print(cnt)

solution()
