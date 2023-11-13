def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

n = int(input())

for i in str(factorial(n))[::-1]:
    if i != '0':
        print(i)
        break
