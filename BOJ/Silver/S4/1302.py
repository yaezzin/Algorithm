from collections import Counter

n = int(input())

dic = dict()
for i in range(n):
    str = input()
    
    if str in dic:
        dic[str] += 1
    else:
        dic[str] = 1

count_dic = Counter(dic)
most_common = count_dic.most_common()
most_common.sort(key=lambda x : (-x[1], x[0]))

print(most_common[0][0])

