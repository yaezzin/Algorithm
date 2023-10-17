from collections import deque

n = int(input())
list = [input().split() for _ in range(n)]

stack = []
for i in range(len(list)):
    for j in range(len(list[i])):
        stack.append(list[i][j][::-1])
    print(*stack)
    stack = []