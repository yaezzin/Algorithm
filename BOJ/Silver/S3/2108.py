from collections import Counter

n = int(input())
lst = [int(input()) for _ in range(n)]

lst.sort()

# 산술 평균
tmp = sum(lst) / len(lst)
print(round(tmp))

# 중앙값
print(lst[len(lst) // 2])

# 최빈값 - 동일할 경우 두번째로 작은 값
count = Counter(lst)
mc = count.most_common()

flag = 0
max_num = mc[0][1]
for i in range(1, len(mc)):
    if max_num == mc[i][1]:
        flag = 1

if flag == 1:
    print(mc[1][0])
else:
    print(mc[0][0]) 

# 범위
print(max(lst) - min(lst))