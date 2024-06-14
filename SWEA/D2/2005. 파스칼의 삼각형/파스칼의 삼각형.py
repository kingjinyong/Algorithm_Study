#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

test = int(input())
for t in range(test):
    ary = []
    for i in range(11):
        ary.append([0] * (11))
    for i in range(11):
        ary[i][1] = 1

    for i in range(1, 11):
        for j in range(1, 11):
            ary[i][j] = ary[i - 1][j - 1] + ary[i - 1][j]

    n = int(input())
    print("#", t+1, sep="")
    for i in range(n):
        for j in ary[i]:
            if j != 0:
                print(j, end=' ')
        print()