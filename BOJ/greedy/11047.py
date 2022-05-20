# 동전 0

n, k = map(int, input().split())
list = []
cnt = 0

for i in range(n):
    num = int(input())
    list.append(num)

list.reverse()

for l in list:
    if l > k:
        continue
    cnt += k // l
    k %= l

print(cnt)

