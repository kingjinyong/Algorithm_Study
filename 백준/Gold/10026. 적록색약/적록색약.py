from collections import deque
import sys
sys.setrecursionlimit(10**9) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯

graph = []
n = int(input())
for i in range(n):
    graph.append(list(map(str, input().strip())))
visited = [[False] * n for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, c):

    visited[x][y] = True


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 있으면서 방문을 안 했고, 맨 처음 넣었던 알파벳과 같다면 또 호출하기
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and c == graph[nx][ny]:
            dfs(nx, ny, graph[nx][ny])

result1 = 0
for color in ['R', 'G', 'B']: # 빨->초->파 순서로 확인
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                result1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * n for _ in range(n)] # 방문표시 초기화
result2 = 0
for color in ['R', 'B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                result2 += 1
print(result1, result2)