import math

BIG_NUM = 10**7

def isPrime(m):
    lst = [True] * (m + 1)
    prime_num = []

    for i in range(2, m + 1):
        if lst[i] == True:
            prime_num.append(i)
            for j in range(i * 2, m + 1 ,i):
                lst[j] = False
    return prime_num


k = int(input())
lst = isPrime(BIG_NUM)
print(lst[k-1])