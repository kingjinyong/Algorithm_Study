def solution(n, lost, reserve):
    dic = {}

    for student in range(1, n+1):
        if student in reserve and student in lost:
            dic[student] = 1
        elif student in lost:
            dic[student] = 0
        elif student in reserve:
            dic[student] = 2
        else:
            dic[student] = 1

    for n in dic:
        if dic[n] == 2:
            if n-1 in dic:
                if dic[n-1] == 0:
                    dic[n] -= 1
                    dic[n-1] = 1
            elif n+1 in dic:
                if dic[n+1] == 0:
                    dic[n] -= 1
                    dic[n+1] = 1
    result = 0
    for i in dic.values():
        if i >= 1:
            result += 1
    # print(dic)
    return result