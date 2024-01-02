n, m = map(int, input().split())

chicken = []
for _ in range(n):
    chicken.append(list(map(int, input().split())))

max_value = 0
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            answer = 0
            for c in chicken:
                answer += max(c[i], c[j], c[k])
        
            max_value= max(answer, max_value)

print(max_value)