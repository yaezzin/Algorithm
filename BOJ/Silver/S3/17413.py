str = input()


word = ""
result = []
flag = False

for s in str:
    # '<' 가 나올 경우 flag를 True로 바꾸고, 이전까지의 단어를 거꾸로 넣는다.
    if s == '<':
        flag = True
        if word:
            result.append(word[::-1])
            word = ""
        result.append(s)

    # '>'가 나올경우 flag를 False로 바꾸고, >만 추가한다  
    elif s == '>':
        flag = False
        result.append(s)
    
    # ' ' 공백의 경우 
    # flag가 True라면 그냥 공백만 넣기
    # flag가 False인 경우에는 거꾸로 넣는다
    elif s == ' ':
        if flag:
            result.append(' ')
        else:
            result.append(word[::-1])
            word = ''
            result.append(' ')
    
    # 괄호가 있는 경우에는 단어를 다 넣고
    # 괄호가 없는 경우에는 문자열을 이어놓는다.
    else:
        if flag:
            result.append(s)
        else:
            word += s

# 만약 남은 단어가 있다면 거꾸로 붙여주기
if word:
    result.append(word[::-1])

print(''.join(result))



