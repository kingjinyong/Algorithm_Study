from itertools import combinations

test = int(input())

for _ in range(test):
    a, b = map(int, input().split())
    child = 1
    parent = 1
    parent_2 = 1

    for i in range(b, 0, -1):
        child *= i
    for i in range(b-a, 0, -1):
        parent_2 *= i
    for i in range(a, 0, -1):
        parent *= i
        
    result = child // (parent*parent_2)
    print(result)