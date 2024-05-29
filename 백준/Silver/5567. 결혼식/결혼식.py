from collections import deque
import sys
sys.setrecursionlimit(10**6) # 재귀에는 무조건 쓰라고 함
input = sys.stdin.readline

n = int(input())
m = int(input())

friends = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

# print(friends)
# print(visited)

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        x = queue.popleft()
        for i in friends[x]:
            if visited[i] == 0:
                visited[i]= visited[x] + 1
                queue.append(i)
bfs(1)
# print(visited)
cnt = 0
for i in visited:
    if i == 2 or i == 3:
        cnt += 1
print(cnt)