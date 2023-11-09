from collections import Counter

n = int(input())
lst = list(map(int, input().split()))

count = Counter(lst)

stack = []
result = [-1] * n

for i in range(n):
    while stack and count[lst[stack[-1]]] < count[lst[i]]:
        index = stack.pop()
        result[index] = lst[i]
    
    stack.append(i)

print(*result)