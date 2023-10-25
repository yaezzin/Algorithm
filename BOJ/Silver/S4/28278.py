n = int(input())

stack = []
for i in range(n):
    command = int(input().split())
    
    if command[0] == "1":
        stack.append(command[1])
    
    elif command[0] == "2":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
            
    elif command[0] == "3":
        print(len(stack))
        
    elif command[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif command[0] == "5":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])