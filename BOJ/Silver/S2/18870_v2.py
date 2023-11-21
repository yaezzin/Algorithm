def binary_search(lst, target):
    # 나보다 작은 놈이 몇개냐?
    start = 0
    end = len(lst) - 1
    
    while start <= end:

        mid = (start + end) // 2

        if lst[mid] == target:
            return mid

        elif lst[mid] < target:
            start = mid + 1
        
        else:
            end = mid - 1

n = int(input())
lst = list(map(int, input().split()))

# 중복 제거해주기
new_lst = sorted(list(set(lst)))

answer = []
for l in lst:
    answer.append(binary_search(new_lst, l))

print(*answer)
