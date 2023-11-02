n = int(input())
listn = list(map(int, input().split()))

dic = dict()
for i in listn:
    dic[i] =1 

m = int(input())
listm = list(map(int, input().split()))

result = dict()
for i in listm:
    if i in dic:
        result[i] = 1
    else:
        result[i] = 0

print(*result.values())
   
