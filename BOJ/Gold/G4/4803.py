def is_cyclic(current_node, parent):
    visited[current_node] = 1
    
    for next_node in tree[current_node]:
        # 방문을 안했고, 이웃 노드가 현재노드와 사이클이 있는지 확인
        if not visited[next_node]: 
            if is_cyclic(next_node, current_node): 
                return True
        
        # 이미 방문을 했지만, 이웃이 부모가 아니라면 싸이클이 존재
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