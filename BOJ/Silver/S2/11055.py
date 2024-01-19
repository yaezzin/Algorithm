def func(n):
    dp = lst.copy()

    for i in range(n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + lst[i])

    return max(dp)

n = int(input())
lst = list(map(int, input().split()))

print(func(n))





