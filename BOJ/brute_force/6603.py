
from itertools import combinations


while True:
    k, *s = list(map(int, input().split())) 

    for i in combinations(s, 6):
        print(*i)
    print()

    if k == 0:
        break
