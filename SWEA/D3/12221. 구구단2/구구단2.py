test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    result = n*m
    print("#", end='')
    print(t, end=' ')
    if n >= 10 or m >= 10:
        print(-1)
    else:
        print(result)