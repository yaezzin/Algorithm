n = int(input())
lst = list(map(int, input().split()))

cnt = [0] * 10

start = 0
end = 0
answer = 0

cnt[lst[0]] += 1
while end != n:
    l = len(list(filter(lambda x: x != 0, cnt)))

    if l <= 2:
        answer = max(answer, end - start + 1)
        end += 1
        if end == n:
            break  
        cnt[lst[end]] += 1
        
        
    else:
        cnt[lst[start]] -= 1
        start += 1

print(answer)