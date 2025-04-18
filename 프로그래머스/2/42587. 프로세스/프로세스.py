from collections import deque

def solution(priorities, location):
    # 인덱스와 우선 순위를 묶어서 새로운 스택에 저장
    stk = []
    for i in range(len(priorities)):
        stk.append([i, priorities[i]])

    # 큐로 변환
    queue = deque(stk)
    
    # 실행한 프로세스의 순서를 저장할 배열 생성
    ary = []
    
    while queue:
        # 대기큐의 첫 번째 인덱스를 뽑아서 배열에 저장
        ary.append(queue.popleft())
        
        a = ary[-1]
        
#         # 나머지 대기큐를 순회해서
#         for q in queue:
#         # 가장 최근 저장된 배열값 우선순위와 비교 후 대기큐의 우선순위가 더 크다면 배열값을 뽑아 대기큐 맨 뒤로 넣기
#             if a[1] < q[1]:
#                 queue.append(ary.pop())
#                 break
        if any(a[1] < q[1] for q in queue):
            queue.append(ary.pop())
        
    cnt = 0
    for a in ary:
        cnt += 1
        if a[0] == location:
            return cnt
                