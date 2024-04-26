import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯

def dfs(x, y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, 1, -1, -1]

    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0    # 방문표시
        for i in range(8):
            dfs(x + dx[i], y + dy[i])

        return True

    return False


while True:
    land = 0
    graph = []
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    for i in range(m):
        graph.append(list(map(int, input().split())))
    # print(graph)

    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                land += 1
    print(land)