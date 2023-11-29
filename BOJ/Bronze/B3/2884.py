h, m = map(int, input().split())

# 만약 분이 45를 뺐을때 음수라면
if m - 45 < 0:
    m = m + 60 - 45
    if h < 1:
        h = 23
    else:
        h -= 1

else:
    m = m - 45

print(h, m)