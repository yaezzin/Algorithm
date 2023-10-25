# 방법 1 : 배열 이용
n = int(input())
list = list(map(int, input().split()))
x = int(input())

l = []

count = 0
for i in list:
    if x - i in l:
        count += 1
    else:
        l.append(i)

print(count)

# 방법 2 이진 탐색
n = int(input())
list = list(map(int, input().split()))
x = int(input())

count = 0
left = 0
right = len(list) -1

list.sort()
while left < right:
    sum = list[left] + list[right]

    if sum == x:
        count += 1
    
    if sum > x:
        right -= 1
    else:
        left += 1
    
print(count)

