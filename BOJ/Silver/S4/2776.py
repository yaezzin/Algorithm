t = int(input())

for i in range(t):
    n = int(input())
    lst1 = list(map(int, input().split()))
    dic1 = dict()
    for i in lst1:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1

    m = int(input())
    lst2 = list(map(int, input().split()))
    dic2 = dict()
    for i in lst2:
        if i in dic2:
            dic2[i] += 1
        else:
            dic2[i] = 1

    for j in lst2:
        if j in dic1:
            print(1)
        else:
            print(0)