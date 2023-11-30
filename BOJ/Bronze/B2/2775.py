def bin(n, k):
    B = [[0 for _ in range(15)]  for _ in range(15)]
    
    for i in range(15):
        for j in range(15):
            # 0층의 i호는 i의 값을 가진다
            if i == 0:
                B[0][j] = j
            
            # i층의 1호는 항상 1의 값을 가진다.
            elif j == 1:
                B[i][1] = 1
            
            # 나머지
            else:
                B[i][j] = B[i-1][j] + B[i][j-1]
    print(B)
    return B[n][k]
    

t = int(input())
for i in range(t):
    n = int(input())
    k = t = int(input())
    print(bin(n, k))