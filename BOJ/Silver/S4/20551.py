import sys
input = sys.stdin.readline

def binary_search(target):
    start, end = 0, len(lst_b) - 1
    res = -1 

    while start <= end:
        mid = (start + end) // 2

        if lst_b[mid] == target:
            res = mid
            end = mid - 1
        
        elif lst_b[mid] > target:
            end = mid - 1

        else:    
            start = mid + 1
    
    return res


n, m = map(int, input().split())
lst_a = [ int(input()) for _ in range(n) ]
lst_b = sorted(lst_a)
for _ in range(m):
    d = int(input())
    print(binary_search(d))

