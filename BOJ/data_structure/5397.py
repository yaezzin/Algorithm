import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    lst = list(input().strip())

    left = []
    right = []

    for l in lst:
        if l == '<':
            if left:
                right.append(left.pop())
        elif l == '>':
            if right:
                left.append(right.pop())
        elif l == '-':
            if left:
                left.pop()
        else:
            left.append(l)

    left.extend(reversed(right))
    print(''.join(left))
    