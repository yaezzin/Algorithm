# DFS
def dfs(current_node):
    visited[current_node] = 1
    answer.append(current_node)

    for next_node in adj[current_node]:
        if visited[next_node] == 0:
            dfs(next_node)

# Logic
n = int(input())
m = int(input())

adj = [ [] for i in range(n+1) ]

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0] * (n+1)
answer = []
dfs(1)
print(len(answer) - 1) # 시작한 컴퓨터는 빼줘야 함