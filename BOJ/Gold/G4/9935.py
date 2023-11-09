input_str = input()
bomb_lst = [i for i in input()]
result = []

for i in range(len(input_str)):
    result.append(input_str[i])
    # 만약 폭발 문자열의 끝부분이랑 지금 내 결과값의 마지막 글자가 동일하다면 pop
    if bomb_lst[-1] == result[-1]:
        # 맨 뒤부터 폭발문자열길이만큼까지의 문자가 bomb이랑 같고,
        # 폭발문자열보다 현재 문자열이 더 길다면 pop할 수 있다.  
        if bomb_lst == result[-len(bomb_lst):] and len(bomb_lst) <= len(result):
            for i in range(len(bomb_lst)):
                result.pop()

if result:
    print(''.join(result))
else:
    print('FRULA')