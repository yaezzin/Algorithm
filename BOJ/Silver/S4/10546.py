n = int(input())

dic = {}
for i in range(n):
    name = input()
    
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
    
for i in range(n-1):
    name = input()

    dic[name] -= 1

for k, v in dic.items():
    if v == 1:
        print(k)