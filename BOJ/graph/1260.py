from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

adjArray = [[False] * n for _ in range(n)]

checkArray_dfs = [False] * n
checkArray_bfs = [False] * n

for _ in range(m):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    adjArray[a][b] = True
    adjArray[b][a] = True

def dfs(currentNode):       
    checkArray_dfs[currentNode] = True    
    print(currentNode + 1, end = " ")  
    
    for nextNode in range(n): 
        if not checkArray_dfs[nextNode] and adjArray[currentNode][nextNode] == True:
            dfs(nextNode)
            
        
def bfs(currentNode):
    checkArray_bfs[currentNode] = True
    q = deque()
    q.append(currentNode)

    while q:
        currentNode = q.popleft()
        print(currentNode + 1, end = " ")

        for nextNode in range(n):
            if not checkArray_bfs[nextNode] and adjArray[currentNode][nextNode] == True:
                q.append(nextNode)
                checkArray_bfs[nextNode] = True
                
                
dfs(v-1)
print()
bfs(v-1)