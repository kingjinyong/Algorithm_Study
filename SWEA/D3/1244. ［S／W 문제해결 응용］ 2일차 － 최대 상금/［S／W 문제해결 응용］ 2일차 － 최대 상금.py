test = int(input())


def dfs(n):
    global answer
    if n == N:
        answer = max(answer, int("".join(map(str, ary))))
        return

    for i in range(L - 1):
        for j in range(i+1, L):
            ary[i], ary[j] = ary[j], ary[i]

            check_number = int("".join(map(str, ary)))
            if (n, check_number) not in visited:
                dfs(n + 1)
                visited.append((n, check_number))
            ary[i], ary[j] = ary[j], ary[i]


for t in range(1, test + 1):
    number, N = map(int, input().split())
    ary = list(str(number))
    answer = 0
    L = len(ary)
    visited = []

    dfs(0)
    print(f"#{t} {answer}")