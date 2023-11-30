n, k = map(int, input().split())
lst = list(map(int, input().split()))

# 1. 합배열 구하기
total = 0
sum_list = []
for i in range(len(lst)):
    total += lst[i]
    sum_list.append(total)

# 2. 합배열에서 수행
c = [0] * k 
count = 0
for i in range(len(sum_list)):
    # 만약 나누어 떨어진다면 이미 0부터 i까지 구간합이 M으로 나누어 떨어지는 것이므로 count++
    tmp = sum_list[i] % k
    if tmp == 0:
        count += 1
    
    # 나누어 지지 않는다면 "나머지가 같은 인덱스"를 증가한다.
    else:
        c[tmp] += 1

# 3. 나머지 값이 같은 합배열의 경우의 수 구하기(?)
# i를 나머지로 가지는 부분 배열 c[i]이 있고,
# 이 부분 배열중에서 2개를 뽑아서 나머지를 0(나누어 떨어지게)을 만들어주어야 함
# 2로 나누어 주는 이유는 중복된 경우를 없애주기 위해서 ex ) [1, 2] [2, 1] 이 동일하다고 여기고 나누어줌
for i in range(k):
    if c[i] > 1:
        count += (c[i] * (c[i] -1) // 2)    


