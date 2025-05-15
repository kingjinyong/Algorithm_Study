test = int(input())

for t in range(1, test + 1):
    N = int(input())
    ary = [0]*31
    ary[1] = 1
    ary[2] = 3
    ary[3] = 5
    for i in range(4, 31):
        ary[i] = ary[i-1] + 2*ary[i-2]
    print(f'#{t} {ary[N//10]}')