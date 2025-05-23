# test = int(input())

for t in range(1, 11):
    test_case = int(input())
    ary = list(map(int, input().split()))
    p = 1
    while True:
        ary[0] -= p
        if ary[0] <= 0:
            ary.pop(0)
            ary.append(0)
            break
        else:
            ary.append(ary.pop(0))

        if p == 5:
            p = 1
        else:
            p += 1

    # print(f"#{t} {answer}")
    print("#", end="")
    print(t, end=" ")
    print(*ary)
