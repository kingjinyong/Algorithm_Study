from collections import deque
qs, s = map(int, input().split())

sary = list(map(int, input().split()))

q = deque()
for i in range(1, qs + 1):
    q.append(i)

m = 0
result = 0
lr = 0
rr = 0
cnt = 0
while sary:
    if q[0] == sary[0]:
        q.popleft()
        sary.pop(0)
    else:
        c1 = q.index(q[-1]) - q.index(sary[0])
        c2 = q.index(sary[0])
        if c1 < c2:
            while q[0] != sary[0]:
                q.rotate(1)
                cnt += 1
        else:
            while q[0] != sary[0]:
                q.rotate(-1)
                cnt += 1
print(cnt)
