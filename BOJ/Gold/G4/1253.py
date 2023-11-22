n = int(input())
lst = list(map(int, input().split()))
lst.sort()

count = 0
for i in range(n):
    start = 0
    end = len(lst) - 1
    
    target = lst[i]
    
    while start < end:
        if lst[start] + lst[end] == target:
            if i != start and i != end:
                count += 1
                break
            
            elif start == i:
                start += 1
            
            elif end == i:
                end   -= 1
        
        elif lst[start] + lst[end] < target:
            start += 1
        
        else:
            end -= 1

print(count)
            