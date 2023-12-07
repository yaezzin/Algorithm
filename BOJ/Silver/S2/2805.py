def binary_search(lst):
    start, end = 0, max(lst)

    while start <= end:
        mid = (start + end) // 2

        s = 0
        for i in lst:
            if i > mid:
                s += i - mid
        
        if s >= m:
            start = mid + 1
       
        else:
            end = mid - 1
    
    return mid

n, m = map(int, input().split())
lst = list(map(int, input().split()))
print(binary_search(lst))