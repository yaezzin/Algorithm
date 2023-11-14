from collections import deque

t = int(input())

# n : 문서의 개수
# m : 몇 번째로 인쇄되었는지 궁금한 문서가 현재 큐에서 몇 번째에 놓여 있는지


for i in range(t):
    n, m = map(int, input().split())
    
    numbers = list(map(int, input().split()))
    queue = deque((i, numbers[i]) for i in range(len(numbers)))

    count = 0
    while queue:
        max_num = max(queue, key=lambda x: x[1])[1]
        first = queue.popleft()

        # 만약 최대값이랑 같으면 count++, 인덱스까지 같으면 종료
        if max_num == first[1]:
            count += 1
            if first[0] == m:
                break 
        
        # 최대값이랑 다르면 큐 오른쪽에 넣기
        if max_num != first[1]:
            queue.append(first)
    
    print(count) 

