def sum_list(str_list):
    sum = 0
    for str in str_list:
        for s in str:
            if s.isdigit():
                sum += int(s)
    return sum

n = int(input())
str_list = [input() for i in range(n)]
str_list.sort(key = lambda x: (len(x), sum_list(x), x))

for i in str_list:
    print(i)