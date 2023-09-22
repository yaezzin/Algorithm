import math

a, b = map(int, input().split())
c, d = map(int, input().split())

up = a * d + b * c 
down = b * d

up = up //math.gcd(up, down)
down = down //math.gcd(up, down)


print(up, down)

