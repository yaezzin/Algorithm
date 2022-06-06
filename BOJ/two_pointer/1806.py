import sys

n, s = map(int, sys.stdin.readline().split()) # 길이 n의 수열, 목표값 s

lst =list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
sum = 0
min_value = sys.maxsize

while start < n and end < n :
    if sum >= s:
        min_value = min(min_value, end - start)
        sum -= lst[start]
        start += 1
    else:
        sum += lst[end]
        end += 1

if min_value == sys.maxsize:
    print(0)
else:
    print(min_value)

    