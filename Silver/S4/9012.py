n = int(input())

for i in range(n):
    str = input()

    list = []
    for s in str:
        if s == '(':
            list.append(s)
        if s == ')':
            if len(list) == 0:
                print('NO')
                break
            else:
                list.pop()
   
    else:
        if len(list) == 0:
            print('YES')
        else:
            print('NO')
