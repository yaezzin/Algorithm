s1 = input()
s2 = input()

alpha = ''.join([i for i in s1 if i.isalpha() ])

if s2 in alpha:
    print(1)
else:
    print(0) 