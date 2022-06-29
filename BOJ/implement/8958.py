t = int(input())

for i in range(t):
    oxList = list(input())
    score = 0
    sumScore = 0

    for ox in oxList:
        if ox == 'O':
            score += 1
            sumScore += score
        else:
            score = 0
    print(sumScore)
