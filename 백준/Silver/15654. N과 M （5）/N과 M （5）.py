from itertools import *
N, M = map(int, input().split())
ary = list(map(int, input().split()))
result = []
for i in permutations(ary, M):
    result.append(i)
result.sort()
for i in result:
    print(*i)