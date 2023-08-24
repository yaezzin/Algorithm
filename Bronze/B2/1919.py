
alpha1 = [0] * 26
alpha2 = [0] * 26

w1 = sorted(input())
w2 = sorted(input())

for w in w1:
    alpha1[ord(w) - ord('a')] += 1

for w in w2:
    alpha2[ord(w) - ord('a')] += 1

count = 0
for i in range(26):
    if alpha1[i] and alpha2[i]:
        count += min(alpha1[i] + alpha2[i])

print(len(w1) + len(w2) - 2 * count)