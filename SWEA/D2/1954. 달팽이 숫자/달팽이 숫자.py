test = int(input())
for t in range(1, test + 1):
    n = int(input())
    ary = [[-1]*n for i in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y, d = 0, 0, 0

    for snail in range(1, n**2+1):
        ary[x][y] = snail
        nx, ny = x + dx[d], y+dy[d]

        if not (0 <= nx < n and 0 <= ny < n) or ary[nx][ny] != -1:
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]

        x, y = nx, ny

    print("#", end='')
    print(t)
    for i in ary:
        print(*i)


