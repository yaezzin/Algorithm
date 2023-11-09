n = int(input())

lst = [input() for _ in range(n)]

count = len(lst)
for word in lst:
    check = []
    for i in range(len(word)):
        # check라는 배열에 하나의 문자가 있었고, 근데 앞글자랑 달라
        if word[i] in check and word[i] != word[i-1]:
            count -= 1
            break
        else:
            check.append(word[i])
            

print(count)


