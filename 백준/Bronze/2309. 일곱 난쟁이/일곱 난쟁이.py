from itertools import combinations
ary = []
for _ in range(9):
    ary.append(int(input()))

for i in combinations(ary, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break