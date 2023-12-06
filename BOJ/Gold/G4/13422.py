t = int(input())

for i in range(t):
    # n 집의 개수
    # m 연속된 집의 개수
    # k 최소 돈의 양 (k를 넘으면 안됨)
    n, m, k = map(int, input().split())

    lst = list(map(int, input().split()))

    if m != n:
        for i in range(m-1):
            lst.append(lst[i])
    
    sum_lst = [0]
    total = 0
    for i in lst:
        total += i
        sum_lst.append(total)
        
    start = 0
    end = m
    count = 0
    while end != len(sum_lst):
        if sum_lst[end] - sum_lst[start] < k:
            count += 1
        
        start += 1
        end += 1
    
    print(count)
    


    
