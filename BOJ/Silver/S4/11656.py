# 11656 접미사 배열

s = input()
list = []
for i in range(len(s)):
    list.append(s[i:])
list.sort()
print(*list, sep='\n')