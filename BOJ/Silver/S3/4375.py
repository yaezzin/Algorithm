# 1, 11, 111 .. 을 n으로 나누었을 때 나머지가 0인 것은?
# n이 3이 주어졌을 때 111 % 3 == 0 이므로 1이 3개 -> 정답 3
# n이 7이 주어졌을 때 111111 % 7 == 0 이므로 1이 6개 -> 정답 6

while True:
    try:
        n = int(input())
    except:
        break

    
    one = 0
    cnt = 1
    while True:
        one = one * 10 + 1 # 1, 11, 111 .. 계속 갱신

        one = one % n

        if one == 0: # 나누어 떨어지면
            print(cnt)
            break

        cnt += 1