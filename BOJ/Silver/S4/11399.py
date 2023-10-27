n = int(input())
list = list(map(int, input().split()))
list.sort()

sum_list = [list[0], ]
for i in range(1, len(list)):
    sum_list.append(list[i] + sum_list[i-1])

print(sum(sum_list))