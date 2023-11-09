s = int(input())

sum = 0
count = 0
for i in range(1, s+1):
    sum += i
    count += 1 

    if sum > s:
        count -= 1
        break
    
print(count)