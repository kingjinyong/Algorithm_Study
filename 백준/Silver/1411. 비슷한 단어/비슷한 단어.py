from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ary = [[] for _ in range(101)]
dic = [{} for _ in range(101)]

for i in range(n):
    num = 0
    m = input().rstrip()

    for j in m:
        if j not in dic[i]:
            dic[i][j] = str(num)
            num += 1

        ary[i] += dic[i][j]
# print(ary)
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if ary[i] == ary[j]:
            count += 1
print(count)
