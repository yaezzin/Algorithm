def solution(board):
    m = 0
    for i in range(n):
        for j in range(n-1):
            swap(board, i, j, i, j+1)
            m = max(m, search(board))
            swap(board, i, j+1, i, j)
    
    for i in range(n-1):
        for j in range(n):
            swap(board, i, j, i+1, j)
            m = max(m, search(board))
            swap(board, i+1, j, i, j)
    
    print(m)

def swap(board, x1, y1, x2, y2):
    tmp = board[x1][y1]
    board[x1][y1] = board[x2][y2]
    board[x2][y2] = tmp

def search(board):
    m = 0    
    # 행기준 최대길이 
    for i in range(n):
        count = 1

        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                count += 1
                m = max(count, m)
            else:
                count = 1
    
    # 열 기준 최대 길이
    for i in range(n):
        count = 1

        for j in range(n-1):
            if board[j][i] == board[j+1][i]:
                count += 1
                m = max(count, m)
            else:
                count = 1
    return m
    
    
n = int(input())
b = [list(input()) for _ in range(n)]
solution(b)
