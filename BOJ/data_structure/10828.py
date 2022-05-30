import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == "push":
        value = word[1]
        stack.append(value)

    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        stack.pop()

    elif order == "size":
        print(len(stack))
    
    elif order == "top":
        if len(stack) == 0:
            print(1)
        print(stack[-1])

    elif order == "empty":
        if len(stack) == 0:
            print(1)
        print(0)

