len_lst = list(map(int, input().split()))
len_lst.sort()

a, b, c = len_lst

if a + b <= c:
    c = a + b - 1

print(a+b+c)