

a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)

list = [0] * 10

for n in num:
    list[int(n)] += 1


for l in list:
    print(l)
