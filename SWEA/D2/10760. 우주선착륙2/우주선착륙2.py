test = int(input())  # 테스트 반복 횟수
for t in range(1, test + 1):
    n, m = map(int, input().split())
    ary = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    result = 0
    for i in range(n):
        for j in range(m):
            possible = 0
            for k in range(8):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < m and ary[i][j] > ary[ni][nj]:
                    possible += 1
            if possible >= 4:
                result += 1

    print("#", end='')
    print(t, end=' ')
    print(result)