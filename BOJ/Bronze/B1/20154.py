from collections import deque

alpha = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3,
    'G': 3, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1,
    'M': 3, 'N': 3, 'O': 1, 'P': 2, 'Q': 2, 'R': 2,
    'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 2, 'X': 2,
    'Y': 2, 'Z': 1
}

s = input()

# 문자열을 덱에 각각 넣음
dq = deque()
for i in range(len(s)):
    dq.append(s[i])

# 각 숫자에 맞게 두개씩 뽑아서 다시 덱에 넣기
n = deque()
while len(dq) > 1:
    n.append(alpha[dq.popleft()] + alpha[dq.popleft()])

# 하나가 남는 경우는 그냥 하나만
if len(dq) != 0:
    n.append(alpha[dq.popleft()])

# 더해진 숫자들을 다시 더하기 + 10을 넘으면 10으로 나눈 나머지로 변경
while len(n) > 1:
    tmp = n.popleft() + n.popleft()
    
    if tmp > 10:
        tmp = tmp % 10

    n.appendleft(tmp)

# 출력
if n[0] % 2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")


