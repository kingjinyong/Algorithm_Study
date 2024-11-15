# test = int(input())
test = 10
for t in range(1, test + 1):
    length = int(input())
    ary = [list(input()) for _ in range(8)]

    result = 0
    # 가로 구하기
    for word in ary:
        for start in range(8 - length + 1):
            if word[start:start + length] == word[start: start + length][::-1]:
                result += 1

    # 세로 구하기
    for i in range(8):
        word = ''.join(ary[j][i] for j in range(8))
        for start in range(8 - length + 1):
            if word[start:start + length] == word[start: start + length][::-1]:
                result += 1


    print("#", end='')
    print(t, end=' ')
    print(result)
