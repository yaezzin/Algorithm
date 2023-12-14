lst = [ [0] * 101 for _ in range(101)]

for i in range(1, 5):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    for x in range(x1, x2):
        for y in range(y1, y2):
            lst[x][y] = i

cnt = 0
for i in range(101):
    for j in range(101):
        if lst[i][j] != 0:
            cnt += 1

print(cnt)