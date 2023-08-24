# 13300 방 배정

n, k = map(int, input().split()) # 참가 학생 수 n, 최대 인원 수 k

list =  [[0 for col in range(6)] for row in range(2)] 

for i in range(n):
    s, y = map(int, input().split()) # 성별 s, 학년 y
    list[s][y-1] += 1

count = 0
for s in range(2):
    for y in range(6):    
        count += (list[s][y] // k) + (list[s][y] % k)

print(count)