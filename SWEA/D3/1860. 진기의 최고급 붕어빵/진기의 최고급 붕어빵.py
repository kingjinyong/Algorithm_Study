from collections import deque
test = int(input())  # 테스트 반복 횟수
for t in range(1, test + 1):
    n, m, k = map(int, input().split())
    people_time = list(map(int, input().split()))
    people_time.sort()

    result = ''
    for i in range(n):
        boong = people_time[i]//m*k # 해당 시간까지 만든 붕어빵 개수
        if boong < i+1: # 해당 시간까지 붕어빵을 만든 개수보다 온 손님의 수가 더 많다면..?
            result = "Impossible"
            break
        result = "Possible"
    print("#", end='')
    print(t, end=' ')
    print(result)