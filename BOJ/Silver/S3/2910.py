from collections import Counter

n, c = map(int, input().split())
list = list(map(int , input().split()))

counts = Counter(list)
common = counts.most_common()

common.sort(key=lambda x : (-x[1]))

result = []
for key, value in common:
    for i in range(value):
        result.append(key)

print(*result)