n, s = map(int, input().split())
lst = list(map(int, input().split()))

# 1. 누적합을 구해놓는다
sum_lst = [0]
total = 0
for l in lst:
    total += l
    sum_lst.append(total)

# 누적합 배열이 0부터 시작하기 때문에 
# start = 1, end = 2 부터 시작하기
# m은 n+1로 최대값으로 만들어 놓기
start = 1
end = 2
m = n + 1

# 만약 누적합 배열의 첫번째에 내가 찾고자하는 값이 있으면 -> 길이가 1인게 있다는 뜻!
if sum_lst[1] == s:
    m = 1

# 그런게 없다면
else:
    # 투포인터로 계속 탐색하기
    while end <= n:
        temp = sum_lst[end] - sum_lst[start-1]

        if temp < s:
            end += 1
        
        elif temp >= s:
            m = min(m, end - start + 1)
            start += 1

# 만약 투포인터로 만들 수 있는게 없다면 0 출력하고, 그렇지 않으면 최소길이  출력
if m == n + 1:
    print(0)
else:   
    print(m)
