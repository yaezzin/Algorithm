# 2960 에라토스테네스의 체

import math

n, k = map(int, input().split())
list = [True] * (n + 1)

count = 0
for i in range(2, n + 1):
    if list[i] == True:
        for j in range(i, n + 1, i):
            if list[j] != False:
                list[j] = False
                count += 1
            
            if count == k:
                print(j)
                break

        