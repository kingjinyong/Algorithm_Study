from collections import deque
import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y):
    global people
    if graph[x][y] == 'P':
        people += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] != 'X':
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)

n, m = map(int, input().split())

graph = []
visited = []
start = []
people = 0
for _ in range(n):
    graph.append(list(input().rstrip()))
    visited.append([False]*m)

# print(graph)
# print(visited)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start = [i, j]

# print(start)

i, j = start

dfs(i, j)

if people == 0:
    print("TT")
else:
    print(people)




