n, c = map(int, input().split())
arr = []
for _ in range(0, n):
    arr.append(int(input()))
arr.sort()

def canInstall(distance):
    cnt = 1
    lastLocation = arr[0]

    for i in range(1, len(arr)):
        locate = arr[i]
        if locate - lastLocation >= distance:
            cnt += 1
            lastLocation = locate
    return  cnt 


start = 1 
end = arr[n - 1] - arr[0] + 1 # 최소거리가 가질 수 있는 최대값
while start <= end:
    mid = (start + end) // 2
    
    if canInstall(mid) < c:
        end = mid
    else:
        start = mid + 1

