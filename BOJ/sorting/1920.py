import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))



for target in targets:

    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2

        if n_list[mid] == target:
            print(1)
            break

        elif n_list[mid] > target:
            right = mid -1
        
        else:
            left = mid + 1
    
    if left > right:
        print(0)
    