n, k = map(int, input().split()) 
lst = list(map(int, input().split()))

# 1. 합배열을 만든다.
sum_list = []
tmp = 0 
for l in lst:
    tmp += l
    sum_list.append(tmp)


# 2. 합배열에서 k 길이만큼의 값을 구해서 리스트에 담고 최대값을 리턴 -> O(N)에 다 해결 가능
answer = [sum_list[k-1], ]
for i in range(1, len(sum_list) - k + 1):
    answer.append(sum_list[k+i-1] - sum_list[i-1])

print(max(answer))