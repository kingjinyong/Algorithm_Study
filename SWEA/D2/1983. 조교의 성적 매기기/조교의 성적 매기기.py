test = int(input())
for t in range(test):
    n, k = map(int, input().split())
    ary = []
    for i in range(n):
        ary.append(list(map(int, input().split())))
    # print(ary)

    score = []
    for i in ary:
        score.append(i[0] * 35 / 100 + i[1] * 45 / 100 + i[2] * 20 / 100)
    # print(score)
    select = score[k - 1]
    score.sort(reverse=True)
    # print(score)
    grade = dict()
    grade = {0: 'A+', 1: 'A0', 2: 'A-', 3: 'B+', 4: 'B0', 5: 'B-', 6: 'C+', 7: 'C0', 8: 'C-', 9: 'D0'}
    # print(grade)

    value = n // 10
    result = score.index(select) // value

    print('#', t+1, ' ', grade[result], sep='')