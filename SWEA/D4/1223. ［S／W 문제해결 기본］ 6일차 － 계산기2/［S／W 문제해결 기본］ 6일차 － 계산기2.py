# test = int(input())
test = 10
for t in range(1, test + 1):
    n = int(input())
    ary = list(input())

    stk = []
    while ary:
        if ary[-1].isdigit():
            stk.append(int(ary.pop()))
        elif ary[-1] == '*':
            ary.pop()
            stk.append(stk.pop()*int(ary.pop()))
        else:
            ary.pop()

    print("#", end='')
    print(t, end=' ')
    print(sum(stk))