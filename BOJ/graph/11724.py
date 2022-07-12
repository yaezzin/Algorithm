import sys
input = sys.stdin.readline

n, m = map(int, input().split())

adjArray = [[False] * n for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    # 0-base로 맞추어줌
    u -= 1
    v -= 1

    # 무방향 그래프이므로 양쪽다 true로 설정해야함
    # adjArray[i][j] == True -> I에서 j로 가는 간선이 존재한다는 뜻
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

answer = 0
for i in range(n):
    if checkArray[i]: # i번째 정점이 방문했다면 continue
        continue
    checkArray[i] = True #방문하지 않았다면 true로 바꾸고 함수 호출
    dfs(i)
    answer += 1

print(answer)