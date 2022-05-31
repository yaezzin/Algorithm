import sys
from collections import Counter

n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()
mid = len(lst)//2

print(round(sum(lst)/n)) # 평균
print(lst[mid]) # 중앙값

count = Counter(lst).most_common() # 최빈값
print(count)
if len(count) > 1 and count[0][1] == count[1][1]: # 횟수 비교
    print(count[1][0])
else:
    print(count[0][0])

print(max(lst) - min(lst)) # 범위