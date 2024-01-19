def func(n):
    if dp[n] != -1:
        return dp[n]
    
    if n <= 3:
        dp[n] = 1
    
    else:
        dp[n] = func(n-2) + func(n-3)
    
    return dp[n]



t = int(input())
for _ in range(t):
    n = int(input())
    dp = [-1] * (n + 1)
    print(func(n))
    






