n = int(input())
lst = sorted(list(map(int, input().split())))

mx = float('inf')
result = (0, 0, 0)

for i in range(0, len(lst) - 2):
    start = i + 1
    end = len(lst) - 1
    
    while start < end:
        s = lst[end] + lst[start] + lst[i]
        
        if abs(s) < mx:
            mx = abs(s)
            result = (lst[i], lst[start], lst[end])
        
        if s < 0:
            start += 1

        else:
            end -= 1

print(result[0], result[1], result[2])
