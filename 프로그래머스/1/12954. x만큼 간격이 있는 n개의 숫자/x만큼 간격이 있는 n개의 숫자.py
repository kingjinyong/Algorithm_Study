def solution(x, n):
    m = x
    answer = [m]
    for i in range(2, n+1):
        m += x
        answer.append(m)
    return answer