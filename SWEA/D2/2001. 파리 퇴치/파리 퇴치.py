test = int(input())
for t in range(1, test + 1):
    n, m = map(int, input().split())
    fly_ary = [list(map(int, input().split())) for _ in range(n)]
    dead_fly = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            dead = 0

            for _i in range(m):
                for _j in range(m):
                    dead += fly_ary[i+_i][j+_j]
            dead_fly.append(dead)
    print("#", end='')
    print(t, end=' ')
    print(max(dead_fly))


