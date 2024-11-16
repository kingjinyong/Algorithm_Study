test = 10  # 테스트 반복 횟수
for t in range(1, test + 1):
    n = int(input())  # 수식의 길이
    word = list(input())

    suffix = []
    op = []
    # 우선 순위
    dic_v = {'*':2, '+':1}

    for i in word:
        if i in dic_v:
            while op and dic_v[op[-1]] >= dic_v[i]:
                suffix.append(op.pop())
            op.append(i)
        else:
            suffix.append(int(i))
    while op:
        suffix.append(op.pop())

    numbers = []
    for i in suffix:
        if i == '+':
            numbers.append(numbers.pop() + numbers.pop())
        elif i == '*':
            numbers.append(numbers.pop()*numbers.pop())
        else:
            numbers.append(i)

    print("#", end='')
    print(t, end=' ')
    print(numbers[-1])

