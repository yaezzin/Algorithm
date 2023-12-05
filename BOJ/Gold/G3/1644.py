n = int(input())

# 소수 구해놓기 
lst = [0] * (n+1)
for i in range(2, n+1):
    lst[i] = i

for i in range(2, n + 1):
    if lst[i] == i:
        for j in range(i*i, n +1, i):
            lst[j] = 0

# 0 인것들은 모두 제거
zero_list = list(filter(lambda x : x != 0, lst))


# 누적합 구하기
total = 0
sum_list = [0]
for i in zero_list:
    total += i
    sum_list.append(total)

# 투포인터로 조회
start = 0
end = 1
answer = 0
while start < len(sum_list) - 1 and end < len(sum_list):
    s = sum_list[end] - sum_list[start]
    
    if s == n:
        answer += 1
        start += 1

    elif s > n:
        start += 1
    
    else:
        end += 1
    
print(answer)