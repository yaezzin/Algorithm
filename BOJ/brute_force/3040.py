import sys
from itertools import combinations

array = []
for _ in range(9):
    array.append(int(sys.stdin.readline()))

impo = sum(array) - 100

for com in combinations(array, 2):
    if sum(com) == impo: # 두 개 뽑은 것이 1000을 뺸 나머지와 같다면 제거
        array.remove(com[0])
        array.remove(com[1])

for a in array:
    print(a)

