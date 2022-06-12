import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
min = 0
max = max(tree)

while min <= max:
    mid = (min + max) // 2
    
    sum = 0
    for t in tree:
        if t > mid :
            sum += (t - mid)

    if sum >= m:
        min = mid + 1
    else:
        max = mid - 1

print(max)
