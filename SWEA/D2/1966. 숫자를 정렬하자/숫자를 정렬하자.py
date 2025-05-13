test = int(input())

for t in range(1, test + 1):
    N = int(input())
    ary = list(map(int, input().split()))

    ary.sort()

    print(f"#{t}", end=" ")
    print(*ary)
