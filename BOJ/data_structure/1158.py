n, k = map(int, input().split())
queue = [i for i in range(1, n+1)]
result = []
tmp = 0

while len(queue) > 0:
    tmp = (tmp + (k-1)) % len(queue)
    result.append(str(queue.pop(tmp)))

print("<%s>" %(", ".join(result)))