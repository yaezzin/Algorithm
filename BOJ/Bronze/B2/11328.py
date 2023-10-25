# 11328 Strfry

n = int(input())

for i in range(n):
    a, b = input().split()

    list = [0] * 26

    for i in a:
        list[ord(i) - ord('a')] += 1
    
    for i in b:
        list[ord(i) - ord('a')] -= 1
    
    for n in list:
        if n:
            print('Impossible')
            break
    
    else:
        print('Possible')
    
    


