from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
dic = {a:0}
if a == b:
    print(1)
else:
    queue = deque([a])

    while queue:
        x = queue.popleft()

        if x == b:
            print(dic[x] + 1)
            break
        if x > b:
            continue

        if x * 2 not in dic:
            dic[x * 2] = dic[x] + 1
            queue.append(x * 2)

        if int(str(x) + '1') not in dic:
            dic[int(str(x) + '1')] = dic[x] + 1
            queue.append(int(str(x) + '1'))

    else:
        print(-1)