n = int(input())
list = [input().split() for _ in range(n)]
list.sort(key=lambda x : (int(x[1]), int(x[0])))
for i in list:
    print(i[0], i[1])