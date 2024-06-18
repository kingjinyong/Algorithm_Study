from collections import deque
import sys
sys.setrecursionlimit(10**9) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯

graph = []

n = int(input())

for i in range(n):
    graph.append(list(map(int, input().split())))
result = [[0]*n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    visited = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if visited[i] == 0 and graph[q][i] == 1:
                result[x][i] = 1
                queue.append(i)
                visited[i] = 1

for i in range(n):
    bfs(i)
    
for i in result:
    print(*i)

# 0 1 0  -> 0 에서 1
# 0 0 1  -> 1 에서 2
# 1 0 0  -> 2 에서 0

# 0 0 0 1 0 0 0 -> 0에서 3
# 0 0 0 0 0 0 1 -> 1에서 6
# 0 0 0 0 0 0 0 -> 2에서 어디도 못 감
# 0 0 0 0 1 1 0 -> 3에서 4, 3에서 5
# 1 0 0 0 0 0 0 -> 4에서 0
# 0 0 0 0 0 0 1 -> 5에서 6
# 0 0 1 0 0 0 0 -> 6에서 2