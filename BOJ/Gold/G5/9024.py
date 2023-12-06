t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    lst = sorted(list(map(int, input().split())))

    # 서로 다른 두 정수의 합이 K에 가장 가까워야하며 가장 가까운게 몇개 있는가
    closet_sum = float('inf')
    count = 0

    # 투포인터
    start = 0
    end = n - 1
    
    while start < end:

        current_sum = lst[start] + lst[end]
        diff = abs(k - current_sum)
        
        # 차이값을 계산해보고 count 증가
        if diff < closet_sum:
            closet_sum = diff
            count = 1

        elif diff == closet_sum:
            count += 1
            
        # 투포인터 조정
        if current_sum >= k:
            end -= 1
        
        else:
            start += 1    
            
    print(count)

        
            