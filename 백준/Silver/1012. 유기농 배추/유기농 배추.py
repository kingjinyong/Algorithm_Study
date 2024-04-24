import sys 
sys.setrecursionlimit(10000)

def dfs(x, y):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0     # 확인한 곳 그냥 0으로 처리 해버리기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                count += 1

    print(count)