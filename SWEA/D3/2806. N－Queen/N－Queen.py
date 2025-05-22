test = int(input())


def dfs(n):
    global ans

    if n == N:
        ans += 1
        return

    for j in range(0, N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n + j] = v3[n - j] = 1
            dfs(n+1)
            v1[j] = v2[n + j] = v3[n - j] = 0


for t in range(1, test + 1):
    N = int(input())
    ans = 0

    v1 = [0] * (2*N)
    v2 = [0] * (2*N)
    v3 = [0] * (2*N)

    dfs(0)
    print(f"#{t} {ans}")
