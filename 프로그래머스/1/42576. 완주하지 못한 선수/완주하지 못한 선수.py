def solution(participant, completion):
    dic = {}
    for i in participant:
        if i in dic:
            dic[i] += 1
        elif i not in dic:
            dic[i] = 1
    
    for i in completion:
        if i in dic:
            dic[i] -= 1
    
    for i in dic:
        if dic[i] == 1:
            answer = i
    return answer