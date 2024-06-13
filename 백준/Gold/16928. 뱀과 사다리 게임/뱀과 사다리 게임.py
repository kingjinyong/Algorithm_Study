# n, k = map(int, input().split())
# p = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯
from collections import deque
from copy import deepcopy

board = [0] * 101
visited = [False] * 101

n, m = map(int, input().split())

ladder = dict()
for i in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

snake = dict()
for i in range(m):
    u, v = map(int, input().split())
    snake[u] = v
# 
# print(ladder)
# print(snake)

def bfs(start):
    queue = deque()
    queue.append(start)

    visited[start] = True

    while queue:
        u = queue.popleft()

        for i in range(1, 7):
            nx = u + i

            if 0 < nx <= 100 and not visited[nx]:
                if nx in ladder:
                    nx = ladder[nx]
                if nx in snake:
                    nx = snake[nx]
                if not visited[nx]:
                    queue.append(nx)
                    visited[nx] = True
                    board[nx] = board[u] + 1
bfs(1)
print(board[100])