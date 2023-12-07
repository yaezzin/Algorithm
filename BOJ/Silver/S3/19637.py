import sys
input = sys.stdin.readline

def binary_search(num):
    start, end = 0, len(chingho) - 1
    
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        
        # 만약 주어진 num이 칭호의 중간값보다 작으면?
        if num <= chingho[mid][1]:
            answer = mid
            end = mid - 1

        else:
            start = mid + 1
       
    
    return chingho[answer][0]

n, m = map(int, input().split())

# 칭호 입력
chingho = []
for _ in range(n):
    c, n = input().split()
    chingho.append([c, int(n)])

chingho.sort(key=lambda x: x[1])

# 숫자 입력
for _ in range(m):
    num = int(input())
    print(binary_search(num))
