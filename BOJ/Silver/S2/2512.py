def binary_search(lst):
    start, end = 1, max(lst)
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        # mid 값 보다 크면 다 mid로 설정하고 더하기
        # mid 값 보다 작으면 그냥 자기 자신 더하기
        s = 0
        for i in lst:
            if i > mid:
                s += mid
            else:
                s += i
        
        if s <= m:
            start = mid + 1
            answer = max(answer, mid)
       
        else:
            end = mid - 1
    
    return answer

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())

print(binary_search(lst))