s = input()

answer = 0
stack = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    
    else:
        stack.pop()
        if s[i-1] == '(':
            answer += len(stack)
        else:
            answer += 1

print(answer)
