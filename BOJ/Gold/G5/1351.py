n, p, q = map(int, input().split())
dic = dict()
dic[0] = 1

def solution(n):
    if n in dic:
        return dic[n]

    else:
        dic[n] = solution(n//p) + solution(n//q)  
        return dic[n]

print(solution(n))