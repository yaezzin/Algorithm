import sys

n = int(sys.stdin.readline())
d = {}

for _ in range(n):
    name, enter = sys.stdin.readline().rstrip().split()
    
    if enter == 'enter':
        d[name] = 'enter'

    else:
        if d[name]: # 이미 존재하면 삭제
            del d[name]

for i in sorted(d, reverse = True):
    print(i)