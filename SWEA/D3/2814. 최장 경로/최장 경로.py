test = int(input())


def dfs(c, v):
    global ans
    ans = max(ans, len(v))

    for i in ary[c]:
        if i not in v:
            dfs(i, v + [i])


for t in range(1, test + 1):
    N, M = map(int, input().split())
    ary = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        ary[a].append(b)
        ary[b].append(a)
    ans = 0

    for i in range(1, N + 1):
        dfs(i, [i])
    print(f"#{t} {ans}")
