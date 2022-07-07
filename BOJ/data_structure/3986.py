n = int(input())

count = 0
for _ in range(n):
    str = input().rstrip()
    stack = []

    for i in range(len(str)):
        if stack and str[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(str[i])

    if not stack:
        count +=1 
print(count)