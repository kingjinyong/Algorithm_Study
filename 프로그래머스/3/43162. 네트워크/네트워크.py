def dfs(n, computers, computer, visited):
    visited[computer] = True
    
    for connect_com in range(len(computers)):
        if computers[computer][connect_com] == 1 and connect_com != computer:
            if visited[connect_com] == False:
                dfs(n, computers, connect_com, visited)
            
    
    
def solution(n, computers):
    cnt = 0
    
    visited = [False for i in range(n)]
    
    for computer in range(len(computers)):
        if visited[computer] == False:
            dfs(n, computers, computer, visited)
            cnt += 1
            
    return cnt
    