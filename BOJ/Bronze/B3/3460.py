def to_binary(n):
    lst = []
    while n > 0:
        lst.append(n % 2)
        n //= 2
    
    return lst

t = int(input())
for _ in range(t):
    n = int(input())

    lst = to_binary(n)
    
    for i in range(len(lst)):
        if lst[i] == 1:
            print(i, end =' ')