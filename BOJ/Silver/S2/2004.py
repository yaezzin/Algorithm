def five(n):
    count = 0

    while n >= 5:
        count += n//5
        n /= 5

    return count

def two(n):
    count = 0

    while n >= 2:
        count += n//2
        n /= 2
        
    return count

n, k = map(int, input().split())
count_five = five(n) - five(n-k) - five(k)
count_two = two(n) - two(n-k) - two(k)
print(int(min(count_five, count_two)))