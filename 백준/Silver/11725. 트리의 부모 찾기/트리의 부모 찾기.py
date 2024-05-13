import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯

t = int(input())
graph = [[] for _ in range(t+1)]
for _ in range(t-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (t+1)
# print(graph)

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)

dfs(1)

for i in range(2, t+1):
    print(visited[i])