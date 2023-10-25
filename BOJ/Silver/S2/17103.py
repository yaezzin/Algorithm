# 골드바흐 파티션

import math

n = 10000001
list = [1] * n

for i in range(2, int(math.sqrt(n)) + 1): 
    if list[i]: 
        for j in range(i * i, n, i): 
            list[j] = 0 

m = int(input())
for i in range(m):
    k = int(input())
        
    count = 0
    for i in range(2, k//2 + 1):
        if list[i] and list[k-i]:
            count+= 1
   
    print(count)