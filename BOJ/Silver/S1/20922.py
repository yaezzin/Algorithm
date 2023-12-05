import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = 0
answer = 0
cnt = [0] * (max(lst) + 1)

while end != len(lst): 
    if cnt[lst[end]] < k:
        cnt[lst[end]] += 1
        end += 1
    
    else:
        cnt[lst[start]] -= 1
        start += 1
    
    answer = max(answer, end - start)

print(answer)