test = int(input())

for t in range(1, test + 1):
    dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    a, b, c, d = map(int, input().split())
    g = c-a

    answer = 0
    if g == 0:
        answer = d - b + 1
    elif g == 1:
        answer = dic[a]-b + d + 1
    else:
        answer += dic[a] - b
        # print(answer)
        for i in range(a+1, a+g):
            answer += dic[i]
            # print(dic[i])
            # print(answer)

        answer += d + 1
        # print(answer)
    print(f"#{t} {answer}")
