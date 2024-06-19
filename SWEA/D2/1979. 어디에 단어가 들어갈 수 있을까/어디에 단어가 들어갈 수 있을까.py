test = int(input())
for t in range(test):
    n, k = map(int, input().split())
    ary = []

    for i in range(n):
        ary.append(list(map(int, input().split())))
    result = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if ary[i][j] == 1:
                cnt += 1
            if ary[i][j] == 0 or j == n - 1:
                if cnt == k:
                    result += 1
                cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if ary[j][i] == 1:
                cnt += 1
            if ary[j][i] == 0 or j == n - 1:
                if cnt == k:
                    result += 1
                cnt = 0
    print('#', t+1, ' ', result, sep='')