import sys

n = int(input())

n_list = list(map(int, sys.stdin.readline().split()))

cnt = 0
for lst in n_list:
    if n != 1:
        for i in range(2, lst + 1):
            if lst % i == 0:
                break
            else :
                cnt += 1 
print(cnt)