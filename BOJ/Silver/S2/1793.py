def func(n):
    if dp[n] != -1:
        return dp[n]
    
    if n < 2:
        dp[n] = 1
    
    else:
        dp[n] = func(n-1) + (func(n-2) * 2)
    
    return dp[n]


while True:
    try:
        t = int(input())
        dp = [-1] * (t + 1)
        print(func(t))  
    except:
        break





