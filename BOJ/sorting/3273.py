import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] + a[j] == x:
            cnt += 1

print(cnt)