def solution(arr):
    stk = []
    stk.append(arr.pop())
    while arr:
        a = arr.pop()
        if stk[-1] != a:
            stk.append(a)
    stk.reverse()
    return stk