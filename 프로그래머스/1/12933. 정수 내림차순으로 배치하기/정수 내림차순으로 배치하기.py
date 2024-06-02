def solution(n):
    ary = list(map(str, str(n)))
    
    ary.sort(reverse=True)
    
    return int(''.join(ary))