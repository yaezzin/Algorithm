words = []
for i in range(5):
    word = input()
    words.append(word)

# 최대 길이 저장
max_len = max(len(word) for word in words)

# 최대길이까지 돌면서 단어 순회
result = ""
for i in range(max_len):
    for word in words:
        if len(word) > i:
            result += word[i]

print(result)