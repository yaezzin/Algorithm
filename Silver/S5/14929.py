# 14929 귀찮아
n = int(input())
list = list(map(int, input().split()))

total = 0
prefix_sum = 0
for i in range(len(list)-1):
    total += list[i]                    # 누적합 
    prefix_sum += total * list[i+1]     # 현재 요소와 그 다음 요소를 곱한 값의 누적 합

print(prefix_sum)
