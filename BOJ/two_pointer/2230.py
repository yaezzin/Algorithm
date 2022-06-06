import sys

n, m = map(int, sys.stdin.readline().split())

lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()

start = 0
end = 0
min_value = sys.maxsize

while start < n and end < n:
    result = lst[end] - lst[start]
    if result >= m:
        min_value = min(lst[end] - lst[start], min_value)
        start += 1
    else:
        end += 1
        
print(min_value)