n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []

def print_num():
    print(*answer)

def choose(cur_num):
    if cur_num == m + 1:
        print_num()
        return

    for i in range(n):
        if cur_num > 1 and answer[-1] > nums[i]:
            continue
        answer.append(nums[i])
        choose(cur_num+1)
        answer.pop()

choose(1)