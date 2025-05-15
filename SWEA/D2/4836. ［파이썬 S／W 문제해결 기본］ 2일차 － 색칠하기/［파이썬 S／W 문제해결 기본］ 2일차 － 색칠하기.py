test = int(input())

for t in range(1, test + 1):
    board = [[0]*10 for i in range(10)]

    paint_count = int(input())

    for painting in range(paint_count):
        a, b, c, d, e = map(int, input().split())
        if e == 1:
            for i in range(b, d + 1):
                for j in range(a, c + 1):
                    if board[i][j] == 2:
                        board[i][j] += e
                    elif board[i][j] == 0:
                        board[i][j] += e
        elif e == 2:
            for i in range(b, d + 1):
                for j in range(a, c + 1):
                    if board[i][j] == 1:
                        board[i][j] += e
                    elif board[i][j] == 0:
                        board[i][j] += e

    answer = 0
    for i in range(10):
        answer += board[i].count(3)
    print(f'#{t} {answer}')