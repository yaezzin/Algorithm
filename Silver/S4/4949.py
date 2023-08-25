

while True:
    str = input()

    if str == '.':
        break

    stack = []
    for s in str:
        if s == '(':
            stack.append(s)
        elif s == '[':            
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')



