test = int(input())
for t in range(1, test + 1):
    h, w = map(int, input().split())
    map_ary = []

    for _ in range(h):
        map_ary.append(list(map(str, input())))

    x = 0
    y = 0
    for i in range(h):
        for j in range(w):
            if map_ary[i][j] in '<>^v':
                x = j
                y = i
    commands_num = int(input())

    commands = input()
    for cmd in commands:
        if cmd == 'S':
            if map_ary[y][x] == '<':
                for _x in range(x-1, -1, -1):
                    if map_ary[y][_x] == '*':
                        map_ary[y][_x] = '.'
                        break
                    elif map_ary[y][_x] == '#':
                        break
            elif map_ary[y][x] == '>':
                for _x in range(x+1, w):
                    if map_ary[y][_x] == '*':
                        map_ary[y][_x] = '.'
                        break
                    elif map_ary[y][_x] == '#':
                        break
            elif map_ary[y][x] == '^':
                for _y in range(y-1, -1, -1):
                    if map_ary[_y][x] == '*':
                        map_ary[_y][x] = '.'
                        break
                    elif map_ary[_y][x] == '#':
                        break
            elif map_ary[y][x] == 'v':
                for _y in range(y+1, h):
                    if map_ary[_y][x] == '*':
                        map_ary[_y][x] = '.'
                        break
                    elif map_ary[_y][x] == '#':
                        break
        if cmd == 'U':
            map_ary[y][x] = '^'
            if y - 1 >= 0 and map_ary[y - 1][x] == '.':
                map_ary[y][x] = '.'
                y -= 1
                map_ary[y][x] = '^'
        if cmd == 'D':
            map_ary[y][x] = 'v'
            if y + 1 < h and map_ary[y + 1][x] == '.':
                map_ary[y][x] = '.'
                y += 1
                map_ary[y][x] = 'v'
        if cmd == 'L':
            map_ary[y][x] = '<'
            if x - 1 >= 0 and map_ary[y][x - 1] == '.':
                map_ary[y][x] = '.'
                x -= 1
                map_ary[y][x] = '<'
        if cmd == 'R':
            map_ary[y][x] = '>'
            if x + 1 < w and map_ary[y][x + 1] == '.':
                map_ary[y][x] = '.'
                x += 1
                map_ary[y][x] = '>'

    print("#", end='')
    print(t, end=' ')
    for i in map_ary:
        print(''.join(i))
