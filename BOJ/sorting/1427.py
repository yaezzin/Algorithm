n = int(input())
lst = list(str(n))
lst.sort(key = int, reverse = True)

for i in lst:
    print(i, end = "")
