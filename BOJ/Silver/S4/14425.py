n, m = map(int, input().split())

dic = dict()
for i in range(n):
    dic[input()] = 1

count = 0
for i in range(m):
    str = input()
    if str in dic:
        count += 1
    
print(count)