# ex ) 4 3 6 8 7 5 2 1
# [1, 2, 3, 4] 까지 들어가고 4 pop => + + + + -
# [1, 2, 3] 상태니까 3 바로 pop    => -
# 6이니까 5, 6 추가하고 pop, 현재 [1, 2, 5] => + + -
# 8이니까 7, 8 추가하고 pop, 현재 [1, 2, 5, 7] => + + -
# 7, 5, 2, 1은 순서대로 pop => - - - -

n = int(input())

j = 1
flag = 0
stack = []
command = []

for i in range(n):
    num = int(input())

    while j <= num:
        stack.append(j)
        command.append('+')
        j += 1
    
    if stack[-1] == num:
        stack.pop()
        command.append('-')
    
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in command:
        print(i)
