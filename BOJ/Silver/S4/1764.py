n, m = map(int, input().split())

# 듣도 못한 사람
dd = dict()
for i in range(n):
    name = input()
    dd[name] = 1

result = dict()
for i in range(m):
    name = input()

    if name in dd:
        result[name] = 1

sorted_result = sorted(result)
print(len(sorted_result))
print(*sorted_result, sep='\n')

