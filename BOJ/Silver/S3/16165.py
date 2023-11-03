n, k = map(int, input().split())

dic = dict()
for i in range(n):
    team_name = input()
    team_count = int(input())

    for i in range(team_count):
        dic[input()] = team_name

sorted_dict = {key:dic[key] for key in sorted(dic)}

for i in range(k):
    q = input()
    m = int(input())

    # 0인 경우 팀 이름 출력
    if m == 1:
        print(sorted_dict[q])

    # 1인 경우 멤버 모두 출력
    else:
        for i in sorted_dict:
            if sorted_dict[i] == q:
                print(i)
        