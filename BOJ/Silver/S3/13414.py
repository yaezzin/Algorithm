n, k = map(int, input().split())

dic = dict()
for i in range(k):
    num = input()
    dic[num] = i

sorted_dic = {key : dic[key] for key in sorted(dic, key=lambda x: dic[x])}

count = 0
for i in sorted_dic:
    if n == count:
        break
    count += 1
    print(i)