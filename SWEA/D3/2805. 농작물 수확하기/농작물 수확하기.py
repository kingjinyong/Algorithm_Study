test = int(input())

for t in range(1, test + 1):
    N = int(input())
    ary = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        if i <= N//2:
            for j in range(N//2-i, N//2+i+1):
                ans += ary[i][j]
        else:
            for j in range(i-N//2, N+N//2-i):
                ans += ary[i][j]
    print(f"#{t} {ans}")
