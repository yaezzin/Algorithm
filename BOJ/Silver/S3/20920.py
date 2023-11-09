n, k = map(int, input().split())

dic = {}
for i in range(n):
    word = input()
    if len(word) >= k:
        dic[word] = dic.get(word, 0) + 1

sorted_dic = sorted(dic.keys(), key=lambda x : (-dic[x], (-len(x), x)))
for w in sorted_dic:
    print(w)