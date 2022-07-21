import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0
for i in range(1, n+1):
    com = combinations(lst, i)
    
    for c in com:
        if sum(c) == s:
            answer += 1

print(answer)