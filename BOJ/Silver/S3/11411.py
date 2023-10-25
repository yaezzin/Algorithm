import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))

# 합배열 만들기
total = 0
sum_list = [0]
for i in range(len(list)):
    total += list[i]
    sum_list.append(total)

# 계산
m = int(input())
for i in range(m):
    a, b = map(int, input().split())

    print(sum_list[b] - sum_list[a-1])