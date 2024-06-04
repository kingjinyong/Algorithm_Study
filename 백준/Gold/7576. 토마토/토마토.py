# n, k = map(int, input().split())
# p = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯
from collections import deque

m, n = map(int, input().split())
# 토마토 창고
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))
# print(tomato)

# 몇 번 째 방문인지 확인 할 리스트
visited = []
for _ in range(n):
    visited.append([0]*m)
# print(visited)

# 상하 좌우 이동 하게 할 리스트
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph):
    queue = deque() # 방문해야 할 안 익은 토마토가 들어있는 큐 생성

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1: # 익은 토마토가 이미 들어있는 칸이라면
                queue.append([i, j])
                visited[i][j] = 0  # 첫번째 방문 표시

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m: # 범위 안 벗어나고
                if tomato[nx][ny] != -1 and tomato[nx][ny] == 0: # 토마토가 들어가있지 않고, 익지 않은 토마토라면?
                    tomato[nx][ny] = 1                          # 익히고
                    visited[nx][ny] = visited[x][y] + 1         # 몇 번째 방문인지 이전에 방문했던 칸의 횟수 + 1
                    queue.append([nx, ny])                      # 방문 할 큐에 추가
                    # for i in range(n):
                    #     print(visited[i])

bfs(tomato)

max = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0: # 방문 할 수 있는곳 다 방문했는데 안 익은 토마토가 있으면 -1 출력하고 종료
            print(-1)
            exit()
        elif visited[i][j] > max: # 가장 마지막으로 방문한 곳 저장하도록 하기
            max = visited[i][j]

print(max)


