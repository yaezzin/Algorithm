n = int(input())

dic = {}

for i in range(n):
    str = input()
    if str in dic:
        dic[str] += 1
    else:
        dic[str] = 1

maxNum = max(dic.values())
maxNumList = []

for i in dic:
    if dic[i] == maxNum:
        maxNumList.append(i)

maxNumList.sort()
print(maxNumList[0]) 
