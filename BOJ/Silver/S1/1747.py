import math

def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isPalindrome(word):
    for left in range(len(word)//2):
        right = len(word) - left - 1

        if word[left] != word[right]:
            return False
    
    return True

n = int(input())
i = n 
# n보다 크거나 같고, 소수이면서, 팰린드롬인 최소값
while True:
    if isPrime(i) and isPalindrome(str(i)):
        print(i)
        break

    i+= 1