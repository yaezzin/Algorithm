from functools import reduce
import math

n = int(input())
list1 = map(int, input().split())
n1 = reduce(lambda x, y: x*y , list1)

m = int(input())
list2 = map(int, input().split())
n2 = reduce(lambda x, y: x*y , list2)

gcd = math.gcd(n1, n2)

if gcd > 100000000:
    print(str(gcd)[-9:])
else:
    print(gcd)