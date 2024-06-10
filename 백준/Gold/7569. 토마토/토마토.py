# n, k = map(int, input().split())
# p = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯
from collections import deque
from copy import deepcopy

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

zero = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                zero += 1
if zero == 0:
    print(0)
    exit()
def bfs(graph):
    queue = deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    queue.append([k, j, i])

    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx ,ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append([nx, ny, nz])
bfs(tomato)
max = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] > max:
                max = tomato[i][j][k]
            elif tomato[i][j][k] == 0:
                print(-1)
                exit()

print(max-1)