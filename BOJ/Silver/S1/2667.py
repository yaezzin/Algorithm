from collections import deque

def bfs(x, y):   
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


n = int(input())
graph = [ list(map(int, input().rstrip())) for _ in range(n) ]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
print(*answer, sep='\n')