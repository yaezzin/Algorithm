n = int(input())

dic = {}
for i in range(n):
    s = list(input().split('.'))[1]

    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
    

dic = dict(sorted(dic.items(), key=lambda x : x[0]))
for k, v in dic.items():
    print(k, v)