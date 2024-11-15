test = int(input())
for t in range(1, test + 1):
    n = int(input())
    ary = [[-1]*n for i in range(n)]

    x, y = 0, 0
    d = 'r'
    snail = 1
    while True:
        if snail == n**2:
            ary[x][y] = snail
            break
        if d == 'r':
            if y + 1 < n and ary[x][y+1] == -1:
                ary[x][y] = snail
                snail += 1
                y += 1
            else:
                ary[x][y] = snail
                d = 'd'
        elif d == 'd':
            if x + 1 < n and ary[x+1][y] == -1:
                ary[x][y] = snail
                snail += 1
                x += 1
            else:
                ary[x][y] = snail
                d = 'l'
        elif d == 'l':
            if y - 1 >= 0 and ary[x][y-1] == -1:
                ary[x][y] = snail
                snail += 1
                y -= 1
            else:
                ary[x][y] = snail
                d = 'u'
        elif d == 'u':
            if x - 1 < n and ary[x-1][y] == -1:
                ary[x][y] = snail
                snail += 1
                x -= 1
            else:
                ary[x][y] = snail
                d = 'r'

    print("#", end='')
    print(t)
    for i in ary:
        print(*i)


