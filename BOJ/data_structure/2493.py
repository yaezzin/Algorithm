n = int(input())
tower = list(map(int, input().split()))
result = [0] * n

for i in range(1, n):
    target = i - 1
    
    while target != -1:
        if tower[target] >= tower[i]: # 이전탑이 더 크면
            result[i] = target + 1 # result에 target의 인덱스 + 1을 넣어줌
            break
        else:
            target = result[target] -1 

print(*result)
