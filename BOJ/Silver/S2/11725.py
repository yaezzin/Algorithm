import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(current_node):
    for next_node in graph[current_node]:
        if not visited[next_node]: # 연결된 노드의 부모가 없다면
            visited[next_node] = current_node # 현재노드를 다음 노드의 부모노드로 설정한다.
            dfs(next_node)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
       
dfs(1)
for i in range(2, n+1):
    print(visited[i])