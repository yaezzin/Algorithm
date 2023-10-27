from collections import Counter

n = int(input())
list = [int(input()) for _ in range(n)]

counts = Counter(list)

most_common = counts.most_common()
print(min(most_common, key=lambda x: (-x[1], x[0]))[0])
