from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 4방향을 돌면서
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 내에 있고 방문을 할 수 있으면(=1)
            if 0 <= x < nx and 0 <= y < ny and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[nx][ny] + 1
    
    return graph[n-1][m-1] # 목적지까지의 거리 리턴!!

print(bfs(0,0))