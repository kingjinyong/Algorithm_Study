from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ary = list(map(int, input().split()))

ary.sort()

p1 = 0
p2 = n - 1

result = 0

while p1 < p2:
    if ary[p1] + ary[p2] <= k:
        p1 += 1
        p2 -= 1
        result += 1
    else:
        p2 -= 1
print(result)