# ATM

import sys

n = int(input()) # 사람의 수

p = list(map(int, input().split())) # 인출하는데 걸리는 시간
p.sort()

for i in len(1, n):
    p[i] += p[i-1]
print(sum(p))

# 만약 3, 1, 4, 3, 2 를 입력하면 정렬 후 1, 2, 3, 3, 4로 만듦
# 그 후 p[i] += p[i-1]을 통해 리스트를 1, 3, 6, 9, 13로 변환 -> 합 구하기