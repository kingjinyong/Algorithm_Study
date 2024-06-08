def solution(n):
    ary = []
    
    for i in range(1, n+1):
        if n % i == 1:
            ary.append(i)
    return min(ary)