list = [int(input()) for _ in range(9)]
list.sort()

result = []
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if sum(list) - list[i] - list[j] == 100:
            result.append(list[i])
            result.append(list[j])
            break

list.remove(result[0])
list.remove(result[1])

print(*list, sep='\n')