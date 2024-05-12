import sys
input = sys.stdin.readline
c = int(input())
for _ in range(c):

    s = int(input())

    arr = []

    for _ in range(s):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()

    t = arr[0][1]
    count = 1
    for i in range(1, len(arr)):
        if arr[i][1] < t:
            count += 1
            t = arr[i][1]
    print(count)