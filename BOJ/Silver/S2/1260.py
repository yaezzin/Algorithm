import sys
input = sys.stdin.readline

def dfs(current_node):
    visited[current_node] = 1
    answer_dfs.append(current_node)

    for next_node in adj[current_node]:
        if visited[next_node] == 0:
            dfs(next_node)

def bfs(start):
    queue = []
    queue.append(start)
    answer_bfs.append(start)
    visited[start] = 1

    while queue:
        current_node = queue.pop(0)
        
        for next_node in adj[current_node]:
            if visited[next_node] == 0:
                queue.append(next_node)
                answer_bfs.append(next_node)
                visited[next_node] = 1   

# Main Logic
n, m, v = map(int, input().split())
adj = [ [] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1, n+1):
    adj[i].sort()

visited = [0] * (n+1)
answer_dfs = []
dfs(v)
print(*answer_dfs)

visited = [0] * (n+1)
answer_bfs = []
bfs(v)
print(*answer_bfs)