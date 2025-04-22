from collections import deque
test = int(input())

for t in range(test):
    N, M = map(int, input().split())
    ary = deque(list(map(int, input().split())))
    ary.rotate(-M)
    print("#", end="")
    print(t+1, ary[0])
