def solution(clothes):
    wearing = {}
    
    for name, kind in clothes:
        if kind in wearing.keys():
            wearing[kind] += [name]
        else:
            wearing[kind] = [name]
    
    answer = 1
    
    for _, value in wearing.items():
        answer *= (len(value) + 1)
    return answer - 1