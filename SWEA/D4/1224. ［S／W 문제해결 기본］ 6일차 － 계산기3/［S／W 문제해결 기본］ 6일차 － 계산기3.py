def change_suffix(string):
    ary = list(string)
    suffix = []  # 후위 표기식 결과 저장
    op = []  # 연산자 스택


    # 연산자 우선순위 정의
    precedence = {'+': 1, '*': 2}

    for a in ary:
        if a == '(':  # 여는 괄호는 무조건 스택에 저장
            op.append(a)
        elif a in precedence:  # 연산자
            # 스택에 있는 연산자의 우선순위와 비교
            while op and op[-1] != '(' and precedence[op[-1]] >= precedence[a]:
                suffix.append(op.pop())
            op.append(a)  # 현재 연산자를 스택에 저장
        elif a == ')':  # 닫는 괄호
            # 여는 괄호가 나올 때까지 스택의 연산자를 출력
            while op and op[-1] != '(':
                suffix.append(op.pop())
            op.pop()  # 여는 괄호 제거
        else:  # 피연산자
            suffix.append(a)  # 피연산자는 바로 출력

    # 스택에 남은 연산자를 모두 출력
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
        elif i == '*':
            numbers.append(numbers.pop()*numbers.pop())
        else:
            numbers.append(int(i))

    print("#", end='')
    print(t, end=' ')
    print(numbers[-1])
