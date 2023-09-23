import math
import sys
input = sys.stdin.readline

# 소수 판별
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+ 1):
        if n % i == 0:
            return False
    return True

# 메인 로직
n = int(input())
for i in range(n):
    m = int(input())
    a, b = m//2, m//2
    count = 0
    while a > 0:
        if isPrime(a) and isPrime(b):
            count += 1
        a -= 1
        b += 1
    print(count)
