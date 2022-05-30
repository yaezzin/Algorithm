import sys

n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(str, sys.stdin.readline().split())))

lst.sort(key = lambda x: x[0])

for i in lst:
    print(i[0], i[1])
