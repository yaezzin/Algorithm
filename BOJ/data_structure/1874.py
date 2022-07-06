n = int(input())

count = 0
stack = []
result = []
msg = True

for i in range(n):
    x = int(input())
    
    while count < x:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        msg = False
        exit(0)

if msg == False:
    print("NO")
else:
    print("\n".join(result))
