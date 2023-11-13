n = input()

if int(n) < 10:
    n = '0' + n[0]


first = n
count = 0
while True:
    tmp = str(int(n[0]) + int(n[-1])) # 2 + 6 = 8
    n = n[-1] + tmp[-1] 

    if n == first:
        count += 1
        break
    else:
        count += 1
    
print(count)