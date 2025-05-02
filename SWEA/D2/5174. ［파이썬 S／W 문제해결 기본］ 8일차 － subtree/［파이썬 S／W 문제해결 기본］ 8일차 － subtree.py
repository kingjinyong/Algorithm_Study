test = int(input())

def pre_order(n):
    global ans
    if n > 0:
        ans += 1
        pre_order(ary_1[n])
        pre_order(ary_2[n])

for t in range(1, test + 1):
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))
    ary_1 = [0]*(e+2)
    ary_2 = [0]*(e+2)
    for i in range(0, len(lst), 2):
        f, s = lst[i], lst[i+1]

        if ary_1[f] == 0:
            ary_1[f] = s
        else:
            ary_2[f] = s
    # print(ary_1, ary_2)

    ans = 0
    pre_order(n)
    print(f"#{t} {ans}")
