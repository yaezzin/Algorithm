n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()

start = 0
end = n - 1
count = 0
while start < end:
    
    sum = lst[start] + lst[end]
    
    if sum > k:
        end -= 1
    else:
        count += end - start
        start += 1

print(count)
