## 1978 소수 찾기

import math


def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False      
    return True

n = int(input())
list = list(map(int, input().split()))

count = 0
for i in list:
    if isPrime(i):
        count += 1

print(count)