def func(i, j):
    if i == 0 :
        return lst[i][j]
    
    if dp[i][j] != -1:
        return dp[i][j]

    down = func(i - 1, j) 
    down_right = func(i - 1, j - 1)

    dp[i][j] =  max(down_right, down) + lst[i][j]

    return dp[i][j]

# 입력 받기
n = int(input())
lst = [[0] * n for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        lst[i][j] = tmp[j]

#  방법 1 dp 배열 채운 후 최대값 찾기
dp = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        dp[i][j] = func(i, j)
    
mx = 0
for i in range(len(dp)):
    for j in range(len(dp[i])):
        mx = max(mx, dp[i][j])
        
print(mx)
    






