# 우유 축제

n = int(input()) # 우유 가게의 수
store = list(map(int, input().split()))

milk = [0, 1, 2] # 딸기, 초코, 바나나 순

cnt = 0
for i in range(n):
    if store[i] == (cnt % 3) :
        cnt +=1
print(cnt)