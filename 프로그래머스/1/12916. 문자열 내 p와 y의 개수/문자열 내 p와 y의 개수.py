def solution(s):
    answer = True
    
    a = s.lower()
    
    p = 0
    y = 0
    
    for i in a:
        if i == 'p':
            p += 1
        elif i == 'y':
            y += 1

    if p == y:
        return True
    else:
        return False