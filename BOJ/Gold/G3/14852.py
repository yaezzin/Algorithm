MOD = 1000000007

n = int(input())

dp = [0] * (n + 1)
dp_sum = [0] * (n + 1)

dp[0] = 1
dp[1] = 2

dp_sum[0] = 1
dp_sum[1] = 3

# O(N) 풀이
# dp[i] = dp[i - 1] * 2 + dp[i - 2] * 3 +
#         2 * (dp[i - 3] + dp[i - 4] + dp[i - 5] + ... dp[0])
# 결국 dp[i] = 2 * sum(dp[:i-1]) + dp[i-2]

for i in range(2, n + 1):
    dp[i] = (2 * dp_sum[i-1] + dp[i-2]) % MOD
    dp_sum[i] = (dp[i] + dp_sum[i-1]) % MOD

print(dp[n])
