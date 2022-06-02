import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

result1 = set(lst)
result2 = list(result1)

result2.sort()

for result in result2:
    print(result)