def f_sum(s):
    lst = list(map(int, s.split('+')))
    return sum(lst)

# '-'를 기준으로 문자열을 나눔    
string = input().split('-')

# + 를 포함하고 있는 문자열만 합을 구해놓음
for i in range(len(string)):
    if '+' in string[i]:
        string[i] = str(f_sum(string[i]))

# 첫번째 값을 기준으로 리스트에 있는 것들을 다 빼줌
answer = int(string[0])
for i in range(1, len(string)):
    answer -= int(string[i])
print(answer)

