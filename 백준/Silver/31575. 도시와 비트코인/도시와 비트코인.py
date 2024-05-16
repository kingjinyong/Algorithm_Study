def dfs(grid, x, y, n, m, visited):
    # 범위를 벗어나거나 방문할 수 없는 칸이면 중단
    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0 or visited[x][y]:
        return False
    # 목표지점에 도달한 경우
    if x == m - 1 and y == n - 1:
        return True
    # 방문 처리
    visited[x][y] = True
    # 동쪽 또는 남쪽으로 탐색
    return dfs(grid, x + 1, y, n, m, visited) or dfs(grid, x, y + 1, n, m, visited)

def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    if dfs(grid, 0, 0, n, m, visited):
        print("Yes")
    else:
        print("No")

solve()
