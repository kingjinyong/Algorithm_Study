def dfs_iterative(maps, x, y, visited):
    stack = [(x, y)]
    total = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while stack:
        cx, cy = stack.pop()

        if visited[cx][cy] == 1:
            continue

        visited[cx][cy] = 1
        try:
            total += int(maps[cx][cy])
        except ValueError:
            continue

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                stack.append((nx, ny))

    return total


def solution(maps):
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    eat = []

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                eat.append(dfs_iterative(maps, i, j, visited))

    if eat:
        return sorted(eat)
    else:
        return [-1]


# 테스트
print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))  # [1, 1, 27]
print(solution(["XXX", "XXX", "XXX"]))                # [-1]
