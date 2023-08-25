n = int(input())

count = 0
for i in range(n):
    str = input()

    stack = []
    for s in str:
        # 스택이 비어있으면 넣기
        if len(stack) == 0:
            stack.append(s)
        # 비어있지 않으면 앞글자와 비교
        elif len(stack) != 0:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)

    if len(stack) == 0:
        count += 1 

print(count)
            