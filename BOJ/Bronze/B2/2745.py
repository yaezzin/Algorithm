# N진법을 10진법으로 바꾸기
# int(string, base) 이용

n, b = input().split()
print(int(n, int(b)))