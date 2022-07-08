str = list(input())

stack = []
count = 0

for i in range(len(str)):
    if str[i] == '(':
        stack.append('(')
    else:
        if str[i-1] == '(':
            stack.pop()  
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)

