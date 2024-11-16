def recur(n, m, cnt):
    if cnt == m:
        return n
    cnt += 1
    return n * recur(n, m, cnt)


test = 10  # 테스트 반복 횟수
for t in range(1, test + 1):
    a = int(input())
    n, m = map(int, input().split())
    result = recur(n, m, 1)
    print("#", end='')
    print(t, end=' ')
    print(result)