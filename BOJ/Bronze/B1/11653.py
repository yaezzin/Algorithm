import math

def factorize(n):
    factor = 2
    factors = []

    while (factor ** 2 <= n):
        while n % factor == 0:
            factors.append(factor)
            n = n // factor
        factor += 1
    
    if n > 1: # 마지막에 남아있는 숫자가 1보다 크다면 소수이기 떄문에 처리
        factors.append(n)
    
    return factors

n = int(input())
for i in factorize(n):
    print(i)
