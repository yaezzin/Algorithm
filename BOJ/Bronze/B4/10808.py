# 10808번 알파벳 개수 

# 입력
word = input().lower()

# 알파벳 개수만큼 리스트 정의
list = [0] * 26

# 숫자 세기
for w in word:
    list[ord(w) - ord('a')] += 1

# 출력
print(' '.join(map(str, list)))