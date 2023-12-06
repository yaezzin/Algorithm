n = int(input())
dic = {}

for i in range(n):
    s = input()[0]

    if s in dic:
        dic[s] += 1
    
    else:
        dic[s] = 1

dic = dict(sorted(dic.items(), key=lambda x : x[0]))

if max(dic.values()) < 5:
    print('PREDAJA')
else:
    result = ''
    for k, v in dic.items():
        if v >= 5:
            result += k
    print(result)


