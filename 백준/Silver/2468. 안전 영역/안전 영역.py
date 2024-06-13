# n, k = map(int, input().split())
# p = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯
from collections import deque
from copy import deepcopy

n = int(input())

# 영역들
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)
mh = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > mh:
            mh = graph[i][j]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, h):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 > nx or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] <= h or visited[nx][ny] == 1:
                continue

            queue.append([nx, ny])
            visited[nx][ny] = 1




safezone = []
for waterh in range(mh):
    zone = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > waterh:
                bfs(i, j, waterh)
                zone = zone+1
    safezone.append(zone)

# print(safezone)
print(max(safezone))




