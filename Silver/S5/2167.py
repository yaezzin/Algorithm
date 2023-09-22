# 2차원 배열의 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[0] * (m+1)]                           # 원본 배열
D = [[0] * (m+1) for _ in range(n+1)]       # 합 배열

# 원본배열 받기
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 합배열 만들기
for i in range(1, n+1):
    for j in range(1, m+1):
        D[i][j] = D[i][j-1] +D[i-1][j] - D[i-1][j-1] + A[i][j]
print(D)

# 계산
k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)