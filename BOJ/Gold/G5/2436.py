import math 
# n : 최대 공약수
# m : 최소 공배수 
# 최소 공배수 = 최대 공약수 a, b * 서로소 

gcd, lcm = map(int, input().split())

num = lcm // gcd
min = 200000000

for a in range(1, num+1):
    b = num // a
    if num % b == 0 and num % a == 0 and math.gcd(a, b) == 1: # a와 b가 서로소여야 함
        if a + b < min:
            min = a + b
            answer = f"{a * gcd} {b * gcd}"

print(answer)
