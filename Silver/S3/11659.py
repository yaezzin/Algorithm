# 구간 합 구하기 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list = list(map(int, input().split()))

# 합배열 만들어 놓기
sum_list = [0]
total = 0
for i in range(len(list)):
    total += list[i]
    sum_list.append(total)

for i in range(m):
    a, b = map(int, input().split())
    print(sum_list[b] - sum_list[a-1])

