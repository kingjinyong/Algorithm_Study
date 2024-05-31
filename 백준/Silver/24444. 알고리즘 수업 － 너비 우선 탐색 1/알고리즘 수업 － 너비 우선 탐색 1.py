# n, k = map(int, input().split())
# p = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯
from collections import deque

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

# print(graph)
# print(visited)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:         # 인접 정점을 오름차순으로 방문한다고 했으니 정점 돌면서 오름차순 정렬 해주기
    i.sort()
# print(graph)
def bfs(x):
    f = 1
    visited[x] = f
    queue = deque([x])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                f+=1
                visited[i] = f
                # print(visited)


bfs(r)
for i in range(1, n+1):
    print(visited[i])