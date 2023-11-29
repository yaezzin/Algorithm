n = int(input())

s = 0
for i in range(1, n+1):
    # 각 자릿수 + 자기 자신
    s = sum(list(map(int, str(i)))) + i

    if s == n:
        print(i)
        break
    
    if i == n:
        print(0)