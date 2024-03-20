def inclination(a, b, c, d):
    i1 = (b[1]-a[1])/(b[0]-a[0])
    i2 = (d[1]-c[1])/(d[0]-c[0])
    return 1 if (i1 == i2) else 0

def solution(dots):
    a, b, c, d = dots
    
    answer1 = inclination(a, b, c, d)
    answer2 = inclination(a, c, b, d)
    answer3 = inclination(a, d, b, c)
    
    if 1 in [answer1, answer2, answer3]:
        return 1
    return 0
    
    
    
    
        
        
        
    