n, m = map(int, input().split())
adj = [[] for i in range(n+1)]
visited = [0] * (n+1)
arrive = False

def dfs(current_node, depth):
    global arrive
    if depth == 5:
        arrive = True
        return

    visited[current_node] = 1
    for next_node in adj[current_node]:
        if not visited[next_node]:
            dfs(next_node, depth + 1)
    
    visited[current_node] = 0

for i in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(n):
    dfs(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
