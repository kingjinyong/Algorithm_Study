test = int(input())
for t in range(1, test+1):
    word = input()
    ary = []
    for w in word:
        if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
            continue
        ary.append(w)
    print("#", end='')
    print(t, end=' ')
    print(''.join(ary))