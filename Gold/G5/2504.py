import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

stack = [] # 인덱스를 저장
result = [0] * n

for i in range(n - 1, -1, -1):
    while stack and list[i] > list[stack[-1]]:
        j = stack.pop()
        result[j] = i +1    
    stack.append(i)
    
print(*result)