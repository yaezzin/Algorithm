s = input().lower()

list = [0] * 26
for i in s:
    list[ord(i)-ord('a')] += 1

if list.count(max(list)) > 1:
    print('?')
else:
    a = list.index(max(list)) + ord('a')
    print(chr(a).upper())
