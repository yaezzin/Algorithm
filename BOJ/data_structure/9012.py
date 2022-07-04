n = int(input())

for _ in range(n):
    stack = []
    str = input()
    isVPS = True

    for s in str:
    
        if s == "(":
            stack.append(s)
    
        elif s == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    
    else:
        if not stack:
            print('YES')
        else:
            print("NO")
