n = int(input())
m = int(input())
lst = [[0] * n for _ in range(n)]
lst[0][0] = n * n

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def solution():
    # 아래 왼 위 오
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    cur_dir = 0
    x, y = 0, 0
    answer_x, answer_y = 0, 0

    for i in range(2, n * n + 1):

        nx = x + dx[cur_dir]
        ny = y + dy[cur_dir]

        if not in_range(nx, ny) or lst[nx][ny] != 0:
            cur_dir = (cur_dir -1 + 4) % 4
        
        x = x + dx[cur_dir]
        y = y + dy[cur_dir]
        
        lst[x][y] = n * n - i + 1

        if lst[x][y] == m:
            answer_x = x
            answer_y = y
    
    for i in range(n):
        for j in range(n):
            print(lst[i][j], end = ' ')
        print()
    
    print(answer_x + 1, answer_y + 1)

solution()
