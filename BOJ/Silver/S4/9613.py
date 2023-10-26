import math

n = int(input())

for i in range(n):
    list = list(map(int, input().split()))
    
    sum = 0
    for j in range(1, len(list)):
        for k in range(j + 1, len(list)):
            sum += math.gcd(list[i], list[k])
    print(sum)