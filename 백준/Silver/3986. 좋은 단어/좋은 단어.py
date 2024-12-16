n = int(input())

result = 0
for _ in range(n):
    string = list(input())
    stk = []
    for i in string:
        if len(stk) != 0 and stk[-1] == i:
            stk.pop()
        else:
            stk.append(i)
    if len(stk) == 0:
        result += 1
print(result)
