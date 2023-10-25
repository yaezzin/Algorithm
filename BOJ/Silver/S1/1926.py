from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0 # 방문한 위치는 0으로 표시
    w = 1 # 넓이 초기값
    
    while queue:
        # 큐에서 하나의 좌표를 꺼냄
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 해당 좌표에서 상하좌우로 이동하면서 이동할 수 있는 경우(범위 내에 있고, 해당 좌표가 1인 경우)
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                # 다음 위치를 큐에 넣고
                queue.append((nx, ny))
                # 방문 표시하기
                graph[nx][ny] = 0
                # 길이 증가
                w += 1
    return w

count = 0
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count += 1
            answer = max(bfs(i, j), answer)

print(count)
print(answer)