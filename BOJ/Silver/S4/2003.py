n, m = map(int, input().split())
list = list(map(int, input().split()))

# 합배열 만들기
total = 0
sum_list = [0]
for i in range(len(list)):
    total += list[i]
    sum_list.append(total)


count = 0
for i in range(len(sum_list)):
    for j in range(i+1, len(sum_list)):
        if sum_list[j] - sum_list[i] == m:
            count += 1

print(count)