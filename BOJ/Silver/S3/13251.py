from fractions import Fraction


n = int(input()) # 색종류
colors = list(map(int, input().split())) # 색별 조약돌 개수
k = int(input()) 

answer = 0
total = sum(colors)

if k > 1:
    for color in colors:
        tmp = 1
        for i in range(k):
            tmp *= Fraction(color - i, total - i)
        
        answer += tmp
else:
    answer = 1

print(float(answer))