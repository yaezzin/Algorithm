# k개의 1을 포함하는 가장 작은 연속된 부분수열 크기
n, k = map(int, input().split())
lst = list(map(int, input().split()))

# 1과 2의 개수를 세기위해서 리스트 선언
cnt = [0] * 3

# 만약 수열의 길이가 1이고, 첫번째 숫자가 1이라면 1 출력하고 끝 
if n == 1 and lst[0] == 1:
    print(1)
    exit()

# 그렇지 않으면 첫번째 숫자 값을 1 증가시켜준다.
else:
    cnt[lst[0]] += 1

# 투포인터로 조회
start = 0
end = 0
answer = n + 1  
while end < n:
    # 만약 범위 내의 1이 적으면 end +1 하고 count 증가
    if cnt[1] < k:
        end += 1
        if end < n:
            cnt[lst[end]] += 1

    # 만약 범위 내의 1이 크면 start에 대한 count 감소 후 start +1
    else:
        answer = min(answer, end - start + 1)
        cnt[lst[start]] -= 1
        start += 1


if answer == n + 1:
    print(-1)
else:
    print(answer)
