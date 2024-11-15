# test = int(input())
test = 10
for t in range(1, test + 1):
    n = int(input())
    ary = list(input())
    result = 1
    stk = []
    while ary:
        if ary[-1] == ')' or ary[-1] == ']' or ary[-1] == '}' or ary[-1] == '>':
            stk.append(ary.pop())
        elif ary[-1] == '(' and stk[-1] == ')':
            ary.pop()
            stk.pop()
        elif ary[-1] == '[' and stk[-1] == ']':
            ary.pop()
            stk.pop()
        elif ary[-1] == '{' and stk[-1] == '}':
            ary.pop()
            stk.pop()
        elif ary[-1] == '<' and stk[-1] == '>':
            ary.pop()
            stk.pop()
        else:
            result = 0
            break


    print("#", end='')
    print(t, end=' ')
    print(result)