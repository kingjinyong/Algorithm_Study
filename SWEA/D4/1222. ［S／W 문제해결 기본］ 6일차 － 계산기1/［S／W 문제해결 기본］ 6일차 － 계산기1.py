def change_suffix(string):
    ary = list(string)
    suffix = []  # 후위 표기식 결과 저장
    op = []  # 연산자 스택


    # # 연산자 우선순위 정의
    # precedence = {'+': 1, '*': 2}

    for a in ary:
        if a == '+':
            op.append(a)
        else:
            suffix.append(a)
    while op:
        suffix.append(op.pop())
    return suffix


test = 10  # 테스트 반복 횟수
for t in range(1, test + 1):
    n = int(input())  # 수식의 길이
    suffix = change_suffix(input())

    numbers = []
    op = []

    for i in suffix:
        if i == '+':
            numbers.append(numbers.pop()+numbers.pop())
        else:
            numbers.append(int(i))
    #     print(numbers)
    # print(suffix)
    # print(numbers)
    print("#", end='')
    print(t, end=' ')
    print(numbers[-1])
