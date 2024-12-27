# 1 5 3 1 2

# 1 1 2 3 5

# 0 1 1 1 0     불만도임
import sys
input = sys.stdin.readline
n = int(input())
ary = []
for i in range(n):
    ary.append(int(input()))
ary.sort()
# print(ary)

cnt = 0
result = 0
for i in ary:
    cnt += 1
    result += abs(cnt - i)
print(result)