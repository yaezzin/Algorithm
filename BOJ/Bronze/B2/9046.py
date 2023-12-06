t = int(input())

for _ in range(t):
    string = input().replace(' ', '')

    dic = {}
    for s in string:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

    m = max(dic.values())
    
    result = []
    for k, v in dic.items():
        if v == m:
            result.append(k)


    if len(result) == 1:
        print(*result)
    else:
        print('?')

    