def is_cyclic(current_node, parent):
    visited[current_node] = 1
    
    for next_node in tree[current_node]:
        # 방문을 안했고, 이웃 노드가 현재노드와 사이클이 있는지 확인
        if not visited[next_node]: 
            if is_cyclic(next_node, current_node): 
                return True
        
        # 다음 노드가 이미 방문되었지만, 
        # 부모 노드가 아니라면, 이는 현재 노드에서 이전에 방문한 다른 경로를 통해 온 노드
        elif next_node != parent:
            return True
    
    return False

case = 1    
while True:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break

    answer = 0
    visited = [0] * (n + 1)
    tree = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e = map(int, input().split())
        tree[s].append(e)
        tree[e].append(s)

    for i in range(1, n+1):
        if not visited[i]:
            if not is_cyclic(i, -1):
                answer += 1

    if answer == 0:
        print(f'Case {case}: No trees.')
    
    elif answer == 1:
        print(f'Case {case}: There is one tree.')
    
    else:
        print(f'Case {case}: A forest of {answer} trees.')
    
    case += 1