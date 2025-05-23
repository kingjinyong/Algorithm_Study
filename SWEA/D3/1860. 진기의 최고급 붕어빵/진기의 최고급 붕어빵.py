test = int(input())

for t in range(1, test + 1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    dic = {}
    for i in range(11112):
        if i in people:
            dic[i] = people.count(i)
    fish = 0
    answer = "Possible"
    for time in range(1, 11111+1):
        if 0 in dic.keys():
            answer = "Impossible"
            break
        if time % M == 0:
            fish += K
        if time in dic.keys():
            if fish-dic[time] < 0:
                answer = "Impossible"
                break
            fish -= dic[time]

    print(f"#{t} {answer}")
