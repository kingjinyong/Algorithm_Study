test = int(input())
def in_order(n):
    global cnt

    if n <= N:
        in_order(n * 2)
        ary[n] = cnt
        cnt += 1
        in_order(n * 2 + 1)


for t in range(1, test + 1):
    N = int(input())
    ary = [0 for i in range(N + 1)]
    cnt = 1
    in_order(1)
    print(f"#{t} {ary[1]} {ary[N // 2]}")
