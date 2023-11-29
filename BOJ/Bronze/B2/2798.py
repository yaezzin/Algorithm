n, m = map(int, input().split())
lst = list(map(int, input().split()))

result = 400000
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
        
            temp = lst[i] + lst[j] + lst[k]

            if temp <= m and abs(m-temp) < abs(m-result):
                result = temp
print(result)