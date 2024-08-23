
t = int(input())
for i in range(t):
    n, k = map(int, input().split())

    ary = list(map(int, input().split()))

    result = 1
    while ary:
        if ary[0] < max(ary):
            ary.append(ary.pop(0))
        else:
            if k == 0:
                break
            ary.pop(0)
            result += 1

        if k > 0:
            k -= 1
        else:
            k = len(ary) - 1
    print(result)
