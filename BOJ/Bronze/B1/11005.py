n, b = map(int, input().split())
s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = ""
while n:
    answer += str(s[n%b])
    n = n // b

print(answer[::-1])
