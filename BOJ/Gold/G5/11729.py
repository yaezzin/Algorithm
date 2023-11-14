def hanoi(n, first, second, third): # n 개의 원판을 x(두번째 매개변수)에서 y(네번째 매개변수)로 옮기는 함수
    if n == 1:
        print(first, third)
        return
    
    hanoi(n-1, first, third, second) # N-1개의 원판을 첫번쨰에서 -> 2번째 기둥으로 옮김
    hanoi(1, first, second, third)   # 1개의 원판을 첫번째에서 마지막 기둥으로 옮김
    hanoi(n-1, second, first, third) # n-1개의 원판을 두번째에서 마지막 기둥으로 옮김

n = int(input())
print(2**n-1)
if n <= 20:
    hanoi(n, 1, 2, 3)