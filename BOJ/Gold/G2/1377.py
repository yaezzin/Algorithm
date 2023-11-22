n = int(input())
lst = []
for i in range(n):
    lst.append((int(input()), i))

sorted_lst = sorted(lst)
   
max = 0                
for i in range(n):
    if max < sorted_lst[i][1] - i:
        max = sorted_lst[i][1] - i

print(max+1)