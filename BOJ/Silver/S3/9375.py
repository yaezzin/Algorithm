from collections import Counter

t = int(input())

for i in range(t):
    n = int(input())

    lst = []
    for j in range(n):
        cloth, type = input().split()
        lst.append(type)
    
    wear_count = Counter(lst)
    
    cnt = 1
    for key in wear_count:
        cnt *= wear_count[key] + 1

    print(cnt-1)
    