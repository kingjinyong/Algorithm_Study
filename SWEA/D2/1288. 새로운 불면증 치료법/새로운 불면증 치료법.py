test = int(input())


for t in range(1, test + 1):
    n = int(input())
    ary = [0]*10
    c = 1
    while 0 in ary:
        n *= c
        for i in str(n):
            ary[int(i)] = 1
        n //= c
        c += 1
    n*=(c-1)
    print(f"#{t} {n}")
