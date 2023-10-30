n = int(input())
l = [input() for _ in range(n)]

# 1. 중복 제거를 위해 set으로 감싼 후 다시 list로 감싸기
list = list(set(l))

# 2. 사전순 정렬 -> 길이순 정렬
list.sort(key=lambda x : (len(x), x))

for i in list:
    print(i) 
