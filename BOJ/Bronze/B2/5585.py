type = [500, 100, 50, 10, 5, 1]

n = int(input())
money = 1000 - n

result = 0
for t in type:
    result += money // t
    money %= t

print(result)
