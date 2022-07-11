from collections import deque

n = int(input())

lst = []
for _ in range(n):
    lst.append(input().rstrip())

for i in range(n):
    dq = deque(lst[i])

    while True:
        dq.append(dq.popleft())
        cycle = "".join(dq)

        if cycle == lst[i]:
            break

        if cycle in lst:
            index = lst.index(cycle)
            lst.pop(index)
            lst.insert(index, lst[i])

lst = set(lst)
print(len(lst))