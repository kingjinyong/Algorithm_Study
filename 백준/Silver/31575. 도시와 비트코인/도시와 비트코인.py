import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯

from collections import deque

def bfs(n, m, graph):
    if graph[0][0] == 0 or graph[m-1][n-1] == 0:
        return "No"

    queue = deque([(0, 0)])
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True

    directions = [(0, 1), (1, 0)]
    while queue:
        x, y = queue.popleft()

        if x == m - 1 and y == n - 1:
            return "Yes"

        # # 남쪽 이동
        # if x + 1 < m and not visited[x + 1][y] and graph[x + 1][y] == 1: # 범위 안 벗어나고, 방문 안 했고, 진우가 갈 수 있는 칸인 경우
        #     visited[x + 1][y] == True
        #     queue.append((x + 1, y))
        #
        # # 동쪽 이동
        # if y + 1 < n and not visited[x][y + 1] and graph[x][y + 1] == 1: # 위와 동일
        #     visited[x][y + 1] == True
        #     queue.append((x, y + 1))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return "No"

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

print(bfs(n, m, graph))