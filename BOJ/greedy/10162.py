t = int(input())

buttons = [300, 60, 10] # 5분, 1분, 10초
cnt = 0
answer = []

for i in buttons:
    
    cnt = t//i
    answer.append(cnt)
    t %= i

if t != 0:
    print(-1)
else:
    print(answer[0], answer[1], answer[2])
