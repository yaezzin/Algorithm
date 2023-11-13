import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

s = input()
result = 0
for i in s:
    if i.isupper():
        result += ord(i)-ord('A') + 27
    else:
        result += ord(i)-ord('a') + 1

if isPrime(result):
    print('It is a prime word.')
else:
    print('It is not a prime word.')