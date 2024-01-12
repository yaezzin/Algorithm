k = int(input())
lst = list(map(int, input().split()))
tree = [[] for _ in range(k+1)]

def func(first, second, depth):
    if first == second:
        tree[depth].append(lst[first])
        return
    
    mid = (first + second) // 2
    tree[depth].append(lst[mid])

    func(first, mid - 1, depth + 1)
    func(mid + 1, second, depth + 1)

    
func(0, len(lst) - 1, 0)

for i in range(k):
    for j in tree[i]:
        print(j, end = ' ')
    print()