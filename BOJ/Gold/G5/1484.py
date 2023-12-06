n = int(input())

answer = []

start = 1
end = 1
flag = 0

while end < 100000:
    tmp = (end ** 2) - (start ** 2)

    if tmp == n:
        answer.append(end)
        flag = 1
        start += 1
    
    elif tmp < n:
        end += 1

    else:
        start += 1

if flag == 0:
    print(-1)

else:
    answer.sort()
    print(*answer, sep='\n')