test = int(input())


def rotate(ary):
    aryR = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            aryR[i][j] = ary[N - 1 - j][i]
    return aryR


for t in range(1, test + 1):
    ary = []
    N = int(input())
    for _ in range(N):
        ary.append(list(map(int, input().split())))

    ary1 = rotate(ary)
    ary2 = rotate(ary1)
    ary3 = rotate(ary2)

    print(f"#{t}")
    for a, b, c in zip(ary1, ary2, ary3):
        print(f'{"".join(map(str, a))} {"".join(map(str, b))} {"".join(map(str, c))}')
