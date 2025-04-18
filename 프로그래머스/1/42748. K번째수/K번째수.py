def solution(array, commands):
    answer = []
    for c in commands:
        s = c[0]-1
        e = c[1]
        find = c[2]-1
        ary = array[s:e]
        ary.sort()
        answer.append(ary[find])
        
    return answer