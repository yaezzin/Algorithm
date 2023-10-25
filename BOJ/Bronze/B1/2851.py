list = [int(input()) for _ in range(10)]

total = 0
sum_list = [0]
for i in range(len(list)):
    total += list[i]
    sum_list.append(total)

close = 0
for i in range(len(sum_list)):
    if abs(100 - sum_list[i]) <= abs(100 - close):
        close = sum_list[i]

print(close)
    
