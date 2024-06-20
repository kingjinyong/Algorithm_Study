from collections import deque
import sys
sys.setrecursionlimit(10**9) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯

m, n, k = map(int, input().split())
area = [[0]*(n) for i in range(m)]
visited = [[False]*(n) for i in range(m)]
# print(area)
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for l in range(x1, x2):
            area[j][l] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(a, b, count):
    visited[a][b] = True
    for i in range(4):
        na, nb = a+dx[i], b+dy[i]
        if 0 <= na < m and 0 <= nb < n and area[na][nb] == 0 and visited[na][nb] == False:
            count = dfs(na, nb, count + 1)
    return count
result = []
for i in range(m):
    for j in range(n):
        if area[i][j] == 0 and visited[i][j] == False:
            cnt = 1
            result.append(dfs(i, j, cnt))
# for i in area:
#     print(i)
print(len(result))
result.sort()
print(*result)