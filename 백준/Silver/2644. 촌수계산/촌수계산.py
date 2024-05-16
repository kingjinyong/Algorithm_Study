import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline    # 입력 때 써줘야 하는 것일 듯
# from collections import deque

n = int(input())
p, s = map(int, input().split())
m = int(input())
graph = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)
chon = [0]*(n+1)
# print(chon)
def dfs(v, i):
    chon[v] = i
    for w in graph[v]:
        if chon[w] == 0:
            dfs(w, i+1)

    # print(chon)
dfs(p, 0)
if chon[s] == 0:
    print(-1)
else:
    print(chon[s])