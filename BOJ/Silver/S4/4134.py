import math
import sys
input = sys.stdin.readline

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False 
    return True

n = int(input())
for i in range(n):
    m = int(input())

    j = 0
    while True:
        if isPrime(m + j):
            print(m + j)
            break
        j += 1
