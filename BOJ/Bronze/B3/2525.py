h, m = map(int, input().split())
s = int(input())

if m + s >= 60:
    h += (m + s) // 60
    m = (m + s) % 60

else:
    m = m + s

if h >= 24:
    h -= 24

print(h, m)