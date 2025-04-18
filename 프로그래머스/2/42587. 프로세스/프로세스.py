from collections import deque

def solution(priorities, location):
    stk = []
    ary = []
    for i in range(len(priorities)):
        stk.append([i, priorities[i]])

    queue = deque(stk)
    
    while queue:
        a = queue.popleft()
        ary.append(a)
        for q in queue:
            if a[1] < q[1]:
                queue.append(a)
                ary.pop()
                break
        
    cnt = 0
    for a in ary:
        cnt += 1
        if a[0] == location:
            return cnt
                