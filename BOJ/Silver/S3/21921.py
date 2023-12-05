import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

# 합배열 만들기
sum_lst = [0, ]
total = 0
for l in lst:
    total += l
    sum_lst.append(total)


# 투포인터
start = 0
end = m 
max = 0
count = 1
while end != len(sum_lst):
    s = sum_lst[end] - sum_lst[start]
    if s >= max:
        if max == s:
            count += 1
        else:
            count = 1
        max = s

    start +=1
    end += 1

if max != 0:
    print(max)
    print(count)
else:
    print('SAD')