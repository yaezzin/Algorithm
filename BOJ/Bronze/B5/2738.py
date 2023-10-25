n, m = map(int, input().split())
list1 = [list(map(int, input().split())) for _ in range(m)]
list2 = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    for j in range(m):
        list1[i][j] += list2[i][j]

for i in list1:
    print(*i)