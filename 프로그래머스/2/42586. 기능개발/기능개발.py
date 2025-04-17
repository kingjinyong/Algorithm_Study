def solution(progresses, speeds):
    progresses.reverse()
    speeds.reverse()
    stk = []
    while progresses:
        cnt = 0
        for i in range(len(speeds)):
            progresses[i] += speeds[i]

        while progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            cnt += 1

            if len(progresses) == 0:
                break

        if cnt != 0:
            stk.append(cnt)
    print(stk)
    return stk
# solution([93, 30, 55], [1, 30, 5]	)
# solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1])