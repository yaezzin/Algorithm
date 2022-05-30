# 단어 정렬

n = int(input())

list = []
for i in range(n):
    if i not in list:
        list.append(input())
    
list.sort(key = len)

for i in list:
    print(i)