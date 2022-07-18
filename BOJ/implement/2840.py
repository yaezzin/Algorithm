n, k = map(int, input().split())

wheel = ["?"] * n
pointer = 0

for _ in range(k):
    s, c = input().split()
    s = int(s)

    pointer = (pointer + s) % n

    # 이동한 곳이 물음표라면 -> 도착한적이 없다는 뜻
    if wheel[pointer] == "?":
        wheel[pointer] = c
    
    elif wheel[pointer] != c:
        print("!")
        exit(0)
    
    if wheel.count(c) >= 2:
        print("!")
        exit(0)

for _ in range(n):
    print(wheel[pointer], end = " ")
    pointer -= 1

    if pointer < 0:
        pointer = n - 1