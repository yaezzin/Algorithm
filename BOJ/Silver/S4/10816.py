from collections import dict

n = int(input())
listn = list(map(int, input().split()))

dictn = dict(int)
for i in listn:
    dictn[i] += 1

m = int(input())
listm = list(map(int, input().split()))

result = []
for i in listm:
    result.append(dictn[i])

print(*result)