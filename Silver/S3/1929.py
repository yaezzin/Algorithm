# 1929 소수 구하기

import math

m, n = map(int, input().split())
list = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if list[i] == True: # i가 소수이면
        for j in range(2*i, n + 1, i):
            list[j] = False


for i in range(m, n+1):
    if list[i] == True:
        print(i)
