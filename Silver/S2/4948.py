# 베르트랑 공준

import math

def isPrime(n):
    list = [True for _ in range(2*n+1)] 
    list[0] = list[1] = False

    for i in range(2, int(math.sqrt(2* n)) + 1):
        if list[i] == True:
            for j in range(i*i, 2*n+1 ,i):
                list[j] = False 

    count = sum(1 for i in range(n + 1, 2 * n + 1) if list[i])
    return count

while True:
    n = int(input())

    if n == 0:
        break
    else:
        count = isPrime(n)
        print(count)

                
                