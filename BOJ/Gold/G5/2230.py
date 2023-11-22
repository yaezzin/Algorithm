import sys

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()

start = 0
end = 0

min_n = sys.maxsize

while start < n and  end < n:
    if lst[end] - lst[start] >=  m:
        min_n = min(lst[end] - lst[start], min_n)
        start += 1
    
    else:
        end += 1
        
print(min_n)