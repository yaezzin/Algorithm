n = int(input())

dic = dict()
for i in range(n):
    name, status = input().split()
    dic[name] = status

sorted_dic = {key:dic[key] for key in sorted(dic, reverse=True)}

for i in sorted_dic:
    if sorted_dic[i] == 'enter':
        print(i)