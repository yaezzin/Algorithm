# 1546 평균


n = int(input())
list = list(map(int, input().split()))
m = max(list)

result = 0
for i in list:
    result += (i / m) * 100

print(result/n)