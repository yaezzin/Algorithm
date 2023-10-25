# 1475 방 번호

num = int(input())

list = [0] * 10
for n in str(num):
    list[int(n)] += 1

six_and_nine = list[6] + list[9]

if six_and_nine % 2 == 0:
    list[6] = list[9] = six_and_nine // 2
else:
    list[6] = list[9] = six_and_nine // 2 + 1

print(max(list)) 

