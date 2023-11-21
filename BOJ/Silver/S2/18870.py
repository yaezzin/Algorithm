n = int(input())
lst = list(map(int, input().split()))

# 중복 제거하고 dictionary로 바꾸기
new_lst = sorted(list(set(lst)))
dic = { new_lst[index] : index for index in range(len(new_lst))}

for n in lst:
    print(dic[n], end = ' ')