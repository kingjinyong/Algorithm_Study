ary = [2, 3, 5, 7, 11]

test = int(input())

for t in range(1, test+1):
    ary_2 = []
    n = int(input())

    for i in ary:
        cnt = 0
        while n%i == 0:
            cnt += 1
            n/=i
        ary_2.append(cnt)

    print('#', end="")
    print(t, end=" ")
    print(*ary_2)