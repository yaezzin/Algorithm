import sys
input = sys.stdin.readline

# 입력
n = int(input())
list = list(map(int, input().split()))

# 합배열
sum_list = [0] * n
for i in range(1, len(list)):
    if list[i-1] > list[i]:
        sum_list[i] = sum_list[i-1] + 1
    else:
        sum_list[i] = sum_list[i-1]

print(sum_list)

# 구간합
k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    print(sum_list[b-1]-sum_list[a-1])

    

