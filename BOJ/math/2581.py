m = int(input())
n = int(input())

prime_lst = []
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(m, n):
    if isPrime(i):
       prime_lst.append(i)

if len(prime_lst) == 0:
    print(-1) 
else:
    print(sum(prime_lst))
    print(min(prime_lst))
    
