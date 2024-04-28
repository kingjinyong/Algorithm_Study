from collections import deque
# 말 이동
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
def bfs(x, y, x_end , y_end):
    q = deque()
    q.append([x, y])
    graph[x][y] = 1

    while q:
        x, y = q.popleft()
        if x == x_end and y == y_end:
            return graph[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    q.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1

t = int(input())
while t:
    l = int(input())
    graph = [[0]*l for _ in range(l)]
    fx, fy = map(int, input().split())
    gx, gy = map(int, input().split())

    if fx == gx and fy == gy:
        print(0)
        t -= 1
        continue
    result = bfs(fx, fy, gx, gy)
    print(result)
    t -= 1
