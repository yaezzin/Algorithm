n = int(input())

dp = [0] * (n + 1)
dp_sum = [0] * (n + 1)

dp[0] = 1
dp[1] = 0

dp_sum[0] = 1

for i in range(2, n + 1):
    dp[i] = dp[i-2] + (2 * dp_sum[i-2])
    dp_sum[i] = (dp[i] + dp_sum[i-2])

print(dp[n])
