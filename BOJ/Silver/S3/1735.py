import math

a, b = map(int, input().split())
c, d = map(int, input().split())

up = a * d + b * c 
down = b * d

gcd_value = math.gcd(up, down)
up = up //gcd_value
down = down // gcd_value

print(up, down)

