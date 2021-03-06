import sys
import heapq

N, K=map(int, sys.stdin.readline().split())
jewel=[]
bag=[]
result=[]
for i in range(N):
  M, V=map(int, sys.stdin.readline().split())
  heapq.heappush(jewel, (M, V))
for i in range(K):
  C=int(sys.stdin.readline())
  bag.append(C)
bag.sort()

possible=[]

for i in bag:
  while len(jewel)!=0 and i>=(jewel[0][0]):
    heapq.heappush(possible, -heapq.heappop(jewel)[1])
  if len(possible)!=0:
    result.append(-heapq.heappop(possible))
  elif len(jewel)==0:
    break
print(sum(result))
출처: https://mptprs.tistory.com/37 [백병원:티스토리]
