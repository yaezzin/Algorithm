def func(n):
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if lst[i]  > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

n = int(input())
lst = list(map(int, input().split()))
print(func(n))





