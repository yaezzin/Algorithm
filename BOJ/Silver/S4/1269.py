a, b = map(int, input().split())
list_a = list(map(int, input().split()))
dict_a = {key: 1 for key in list_a}

list_b = list(map(int, input().split()))
dict_b = {key: 1 for key in list_b}

count1 = 0
for i in dict_a:
    if i in dict_b:
        count1 += 1

a_minus_b = len(dict_a) - count1

count2 = 0
for i in dict_b:
    if i in dict_a:
        count2 += 1

b_minus_a = len(dict_b) - count2

print(a_minus_b+b_minus_a)