for i in range(3):
    lst = list(map(int, input().split()))
    
    count_zero = lst.count(0)
    
    if count_zero == 0:
        print('E')
    elif count_zero == 1:
        print('A')
    elif count_zero == 2:
        print('B')
    elif count_zero == 3:
        print('C')
    elif count_zero == 4:
        print('D')