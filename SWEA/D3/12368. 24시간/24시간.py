test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    print("#", end='')
    print(t, end=' ')
    print((n + m) % 24)
