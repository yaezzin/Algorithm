n, m = map(int, input().split())

ns = set()
ms = set()

for _ in range(n):
    ns.add(input())

for _ in range(m):
    ms.add(input())

result = sorted(list(ns & ms)) #교집합

print(len(result))
for r in result:
    print(r)