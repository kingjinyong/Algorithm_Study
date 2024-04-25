import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

n, m = map(int , input().split())
visited = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
# print(visited)
# print(graph)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

count = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        count += 1
print(count)
