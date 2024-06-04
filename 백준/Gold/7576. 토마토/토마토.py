# n, k = map(int, input().split())
# p = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯
from collections import deque

m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))
# print(tomato)

visited = []
for _ in range(n):
    visited.append([0]*m)
# print(visited)

queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i, j])
                visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] != -1 and tomato[nx][ny] == 0:
                    tomato[nx][ny] = 1
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                    # for i in range(n):
                    #     print(visited[i])

bfs(tomato)

max = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        elif visited[i][j] > max:
            max = visited[i][j]

print(max -1)


