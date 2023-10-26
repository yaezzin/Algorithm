max = 1000000

dp = [1] * (max + 1)
s = [0] * (max + 1)

for i in range(2, max+1):
    j = 1
    while i*j <= max:
        dp[i*j] += i
        j += 1

for i in range(1, max+1):
    s[i] = s[i-1] + dp[i]

n = int(input())
answer = []
for _ in range(n):
    a = int(input())
    answer.append(s[a])

print('\n'.join(map(str, answer))+'\n')