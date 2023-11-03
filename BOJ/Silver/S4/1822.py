from collections import Counter

n, m = map(int, input().split())

input_list1 = map(int, input().split())
input_list2 = map(int, input().split())

dic1 = dict(Counter(input_list1))
dic2 = dict(Counter(input_list2))
print(dic2)

result = [key for key, value in dic1.items() if value != 0]
result.sort()

if len(result) == 0:
    print(0)
else:
    print(len(result))
    print(*result)
