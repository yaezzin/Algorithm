# 1676 팩토리얼 0의 개수

import math

n = int(input())
factorial = str(math.factorial(n))


count = 0
for i in factorial[::-1]:
    if i == '0':
        count += 1
    else:
        break

print(count)