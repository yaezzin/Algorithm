import math

n, s = map(int, input().split())
list = list(map(int, input().split()))

# 거리의 절대값을 구하기
distance  = []
for i in list:
    distance.append(abs(s-i))

# 거리의 gcd 구하기
min_d = distance[0]
for i in range(1, len(distance)):
    min_d = math.gcd(distance[i], min_d)

print(min_d)