import math

n, m = map(int, input().split())
print(n + m - math.gcd(m, n))