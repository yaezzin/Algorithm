# 대회 or 인턴

n, m, k = map(int, input().split())
cnt = 0

while True:
    if(n >= 2 and m >=1 and n + m - 3 >= k):
        n -= 2
        m -= 1
        cnt += 1
    else:
        break

print(cnt)
    

