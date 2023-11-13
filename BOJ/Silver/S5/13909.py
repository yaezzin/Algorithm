n = int(input())

""" 첫번째 방법
- 메모리 초과 
- N의 범위가 2,100,000,000이기 떄문이다 - 21억개의 배열을 만들면 당연히 메모리 초과가 남
- 그래서 아래 코드를 N을 16으로 해서 돌려보면 어떤 수의 제곱수의 개수만큼 창문이 열려있음

lst = [0] * (n + 1)
for i in range(1, len(lst)):
    for j in range(i, n + 1, i):
        if lst[j] == 0:
            lst[j] = 1

        else:
            lst[j] = 0
        
        print()

print(lst.count(1))
"""

print(int(n**0.5))