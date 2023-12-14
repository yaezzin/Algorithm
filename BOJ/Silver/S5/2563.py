MAX_R = 100

n = int(input())

checked = [[0] * (MAX_R + 1) for _ in range((MAX_R + 1))]
for i in range(n):
    x1, y1 = tuple(map(int, input().split()))

    for x in range(x1, x1 + 10):
        for y in range(y1, y1 + 10):
            checked[x][y] = 1

cnt = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if checked[i][j] == 1:
            cnt += 1

print(cnt)