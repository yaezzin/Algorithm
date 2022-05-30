import sys

n = int(sys.stdin.readline())
lst = []

for i in range(2):
    lst.append(list(map(int, sys.stdin.readline().split())))

print(lst)

lst.sort(key = lambda x: x[0]) # x[1]순으로 먼저 정렬 

result = 0
for i in lst:
    result += i[0] * i[1]