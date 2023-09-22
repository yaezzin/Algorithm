n = int(input())
list = list(map(int, input().split()))

stack = []
result = [-1] * n

for i in range(n):
    while stack and list[stack[-1]] < list[i]:
        index = stack.pop()    
        result[index] = list[i]
    stack.append(i)


print(*result)