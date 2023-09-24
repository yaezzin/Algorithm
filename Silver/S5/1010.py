# func
def bin(n, k):
    if k > n // 2:
        k = n - k
    
    list = [0] * (k + 1)
    list[0] = 1

    for i in range(1, n+1):
        j = min(i, k)
        while j > 0:
            list[j] = list[j] + list[j-1]
            j -= 1
    
    return list[k]

# main
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    print(bin(M, N))