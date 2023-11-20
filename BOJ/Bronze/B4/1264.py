arr = ['a', 'e', 'i', 'o', 'u']
while True:
    str = input()

    if str == '#':
        break

    count = 0
    for s in str:
        if s.lower() in arr:
            count += 1

    print(count)