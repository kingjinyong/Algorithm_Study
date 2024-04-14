import collections
w = []
for _ in range(4):
    w.append(collections.deque(list(input())))

K = int(input()) # 회전 횟수
R = [list(map(int, input().split())) for _ in range(K)]

# 왼쪽 톱니바퀴 확인
def left(num, direction):
    if num < 0: # 첫번째 톱니는 확인 안 함
        return
    if w[num][2] != w[num+1][6]: #극이 다르다면?
        left(num-1, -direction) # 그 왼쪽 톱니바퀴도 조사
        w[num].rotate(direction) # 현재 톱니바퀴는 회전

# 오른쪽 톱니바퀴 확인
def right(num, direction):
    if num > 3:  # 마지막 톱니는 확인 안함
        return
    if w[num][6] != w[num - 1][2]:  # 극이 다르다면?
        right(num + 1, -direction)  # 그 오른쪽 톱니바퀴도 조사
        w[num].rotate(direction)  # 현재 톱니바퀴는 회전

for i in range(K):
    num = R[i][0] - 1 #돌아가는 톱니바퀴
    direction = R[i][1] # 시게, 반시계방향
    left(num-1, -direction) # 왼쪽 조사
    right(num+1, -direction) # 오른쪽 조사
    w[num].rotate(direction) # 현재 톱니바퀴는 회전

res = 0 # 점수
if w[0][0] == '1':
    res += 1
if w[1][0] == '1':
    res += 2
if w[2][0] == '1':
    res += 4
if w[3][0] == '1':
    res += 8

print(res)