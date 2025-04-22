from collections import deque
test = int(input())

for t in range(test):
    s = set(list(input()))
    ary = list(input())
    d = {}

    for i in ary:
        if i in s:
            d[i] = d.get(i, 0) + 1

    print("#", end="")
    print(t+1, max(d.values()))