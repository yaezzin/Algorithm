def solution(lst, search_num):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if lst[mid] < search_num:
            start = mid + 1

        elif lst[mid] > search_num:
            end = mid - 1

        elif lst[mid] == search_num:
            return 1
    
    return 0
        
# Main Logic
n1 = int(input())
lst1 = sorted(list(map(int, input().split())))

n2 = int(input())
lst2 = list(map(int, input().split()))

for l in lst2:
    print(solution(lst1, l))

