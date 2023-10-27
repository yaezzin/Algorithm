import sys
input = sys.stdin.readline

n = int(input())
list = [0] * 1000001

for _ in range(n):
    m = int(input())
    list[m] += 1

for i in range(1000000, 0, -1):
    for j in range(list[i]):
        print(i)

