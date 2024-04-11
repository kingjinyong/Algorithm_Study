n, k = map(int, input().split())

ary = []

for i in range(2, n+1):
    for j in range(i, n+1):
        if j % i == 0:
            if j not in ary:
                ary.append(j)
print(ary[k-1])