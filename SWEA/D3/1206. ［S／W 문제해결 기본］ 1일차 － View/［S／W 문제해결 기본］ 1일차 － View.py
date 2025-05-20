# test = int(input())
test = 10
for t in range(1, test + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-2):
        if lst[i] >= max(lst[i-2], lst[i-1], lst[i+1], lst[i+2]):
            answer += lst[i] - max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
    print(f'#{t} {answer}')
