test = int(input())
for t in range(1, test+1):
    n = int(input())
    ary = list(map(int, input().split()))
    average = sum(ary) // n
    result = 0
    for i in ary:
        if i <= average:
            result += 1
    print("#", end='')
    print(t, end=' ')
    print(result)