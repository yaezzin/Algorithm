n = int(input())
a, b = map(int, input().split())
c = int(input())

adj = [[] for i in range(n+1)]
visited = [0] * (n+1)
arrive = False
answer = -1

def dfs(current_node, depth, end):
    global answer

    if current_node == end:
        answer = depth
        return

    visited[current_node] = 1
    for next_node in adj[current_node]:
        if not visited[next_node]:
            dfs(next_node, depth + 1, end)
    
    visited[current_node] = 0

for i in range(c):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

dfs(a, 0, b)
print(answer)
