import sys

n = int(sys.stdin.readline())

queue = []
for i in range(n):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == "push":
        value = word[1]
        queue.append(value)

    elif order == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif order == "size":
        print(len(queue))
    
    elif order == "front":
        if len(queue) == 0:
            print(-1)
        print(queue[0])
    
    elif order == "back":
        if len(queue) == 0:
            print(-1)
        print(queue[-1])

    elif order == "empty":
        if len(queue) == 0:
            print(1)
        print(0)