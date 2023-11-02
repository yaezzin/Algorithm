n, m = map(int, input().split())

dic = dict()
for i in range(1, n+1):
    j = input()
    dic[str(i)] = j
    dic[j] = i

for i in range(m):
    k = input()
    print(dic[k])
