test = int(input())
for t in range(1, test+1):
    a = 1
    b = 1
    word = input()
    for i in word:
        if i == "L":
            b = a + b
        elif i == "R":
            a = a + b
    print("#", end='')
    print(t, end=' ')
    print(a, b)