n = int(input())
lst = []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    lst.append([num, cnt1, cnt2])

answer = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k:
                continue

            tmp = i * 100 + j * 10 + k
            flag = 1

            for l in lst:
                n, c1, c2 = l

                count_position, count_value = 0, 0
                for digit1, digit2 in zip(str(tmp), str(n)):
                    if digit1 == digit2:  # 같은 위치에 존재하는 경우
                        count_position += 1
                    
                    elif digit1 in str(n):  # 같은 위치는 아니지만 동일한 숫자를 가진 경우
                        count_value += 1

                if c1 != count_position or c2 != count_value:
                    flag = 0
                    break

            if flag == 1:
                answer.append(tmp)

print(len(answer))
