n = int(input())

fibo = [0, 1]
mod = 10 ** 6               # 나누는 수
period = 15 * mod // 10     # 주기

for i in range(2, period):
    fibo.append((fibo[i-1] + fibo[i-2]) % mod)

print(fibo[n % period])