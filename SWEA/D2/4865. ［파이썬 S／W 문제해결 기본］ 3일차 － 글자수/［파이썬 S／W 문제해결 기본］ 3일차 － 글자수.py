from collections import deque
test = int(input())

for t in range(test):
    s = set(list(input()))
    ary = list(input())
    d = {}

    for i in ary:
        if i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

    print("#", end="")
    print(t+1, max(d.values()))