n = int(input())
m = int(input())

adjArray = [[False] * n for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())

    u -= 1
    v -= 1

    adjArray[u][v] = True
    adjArray[v][u] = True   

checkArray = [False] * n

def dfs(currentNode):
    for nextNode in range(n): # 현재 정점에서 갈 수 있는 모든 노드를 확인
        if checkArray[nextNode]:
            continue

        if not adjArray[currentNode][nextNode]: # 방문하지 않았더라도 연결되어있는지 확인해줘야함!
            continue
            
        checkArray[nextNode] = True
        dfs(nextNode)


dfs(0)

answer = -1
for i in checkArray: # i번째 정점이 방문했다면 continue
    if i:
        answer += 1
    
print(answer)