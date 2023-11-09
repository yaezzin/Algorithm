n = int(input())

input_str = input()
input_num = [int(input()) for i in range(n)]

stack = []
for s in input_str:    
    if s.isalpha():
        stack.append(input_num[ord(s)-ord('A')])
    
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        
        if s == '*':
            stack.append(str1 * str2)
        
        elif s == '/':
            stack.append(str1 / str2)
       
        elif s == '-':
            stack.append(str1 - str2)
        
        elif s == '+':
            stack.append(str1 + str2)

print('%.2f' %stack[0])