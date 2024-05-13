n = int(input())    # 컴퓨터 개수
v = int(input())    # 연결 선 개수
graph = [[] for i in range(n+1)]    # 그래프 초기화
visited = [0] * (n + 1) # 방문 표시

for i in range(v): # 그래프 생성
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 -> 양방향

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

dfs(1)

print(sum(visited) - 1)