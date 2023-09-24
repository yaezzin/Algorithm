def bin(n, m):
    if m > n // 2:
        m = n - m
    
    list    = [0] * (m + 1)
    list[0] = 1

    for i in range(1, n+1):
        j = min(i, m)
        while j > 0:
            list[j] = list[j] + list[j-1]
            j -= 1

    return list[m]

n, m = map(int, input().split())
print(bin(n, m))


from itertools import permutations

l, k = map(int, input().split())
print(len(permutations()))
