def solution(n, b):
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ''

    while n > 0:
        n, mod = divmod(n, b)
        result += str(s[mod])

        return result[::-1]

print(solution(-13, -2))