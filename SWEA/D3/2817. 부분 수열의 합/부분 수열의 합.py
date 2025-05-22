test = int(input())


def dfs(tt, n):
    global ans

    if tt > K:
        return

    if n == N:
        if tt == K:
            ans += 1
        return

    dfs(tt + ary[n], n + 1)
    dfs(tt, n + 1)


for t in range(1, test + 1):
    N, K = map(int, input().split())
    ary = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print(f"#{t} {ans}")
