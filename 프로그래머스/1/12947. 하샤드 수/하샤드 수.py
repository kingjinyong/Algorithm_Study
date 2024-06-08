def solution(x):
    x = str(x)
    add = 0
    for i in x:
        add += int(i)
    
    if int(x) % add == 0:
        return True
    else:
        return False