def solution(s):
    stk1 = list(s)
    stk2 = []
    
    while stk1:
        a = stk1.pop()
        if a == '(':
            if stk2 and stk2[-1] == ')':
                stk2.pop()
            elif not stk2:
                return False
        else:
            stk2.append(a)
    if len(stk1) == 0 and len(stk2) == 0:
        return True
    else:
        return False
                