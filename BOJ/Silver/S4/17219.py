from collections import Counter

n, k = map(int, input().split())
dic = dict()

for i in range(n):
    a, b = input().split()
    dic[a] = b

for i in range(k):
    print(dic[input()])

