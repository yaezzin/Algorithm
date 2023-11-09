input_string = input()

stack = []
for s in input_string:
    if s.isalpha():
        if s.isupper():
            if ord(s) + 13 < 91:
                stack.append(chr(ord(s) + 13))
            else:
                stack.append(chr(65 + 13 - (90 - ord(s) + 1)))
        else:
            if ord(s) + 13 < 123:
                stack.append(chr(ord(s) + 13))
            else:
                stack.append(chr(97 + 13 - (122 - ord(s) + 1)))
    
    elif s.isnumeric():
        stack.append(s)
    
    else:
        stack.append(' ')


print(*stack, sep='')