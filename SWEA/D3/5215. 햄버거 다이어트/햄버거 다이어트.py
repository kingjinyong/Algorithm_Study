test = int(input())


def dfs(n, l, t):
    global mt

    if l > L:
        return

    if mt < t:
        mt = t

    if n == N:
        return

    taste, kcal = ary[n]

    dfs(n + 1, l + kcal, t + taste)
    dfs(n + 1, l, t)


for t in range(1, test + 1):
    N, L = map(int, input().split())

    ary = [list(map(int, input().split())) for _ in range(N)]

    mt = 0
    dfs(0, 0, 0)

    print(f"#{t} {mt}")
