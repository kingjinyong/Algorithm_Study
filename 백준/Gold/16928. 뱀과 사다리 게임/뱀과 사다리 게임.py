# n, k = map(int, input().split())
# p = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())

ladder = dict()
for i in range(n):
    u, v = map(int, input().split())
    ladder[u] = v

snake = dict()
for i in range(m):
    u, v = map(int, input().split())
    snake[u] = v

board = [0]*101
visited = [False]*101
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        x = queue.popleft()

        for i in range(1, 7):
            nx = x + i
            if 0 < nx <= 100 and not visited[nx]:
                if nx in ladder:
                    nx = ladder[nx]
                if nx in snake:
                    nx = snake[nx]
                if not visited[nx]:
                    queue.append(nx)
                    visited[nx] = True
                    board[nx] = board[x] + 1



bfs(1)
print(board[100])