from collections import deque

test = int(input())

for t in range(1, test + 1):
    left_q = deque([])
    right_q = deque(list(input()))
    # print(left_q, right_q)
    left_q.append(right_q.popleft())
    while right_q:
        if not left_q or  left_q[-1] != right_q[0]:
            left_q.append(right_q.popleft())
        elif left_q[-1] == right_q[0]:
            left_q.pop()
            right_q.popleft()

    print(f"#{t} {len(left_q)}")
