test = int(input())


def post_order(l):
    if l <= N:
        if ary[l] == 0:
            ary[l] = post_order(l * 2) + post_order(l * 2 + 1)
        return ary[l]
    else:
        return 0


for t in range(1, test + 1):
    N, M, L = map(int, input().split())
    ary = [0] * (N + 1)
    # print(ary)
    for i in range(M):
        a, b = map(int, input().split())
        ary[a] = b
    # print(ary)

    answer = post_order(L)
    print(f'#{t} {answer}')
