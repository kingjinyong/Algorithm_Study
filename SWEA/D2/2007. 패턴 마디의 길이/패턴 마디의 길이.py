test = int(input())
for t in range(test):
    n = input()
    for i in range(1, 31):
        ary = []
        for j in range(0, len(n), i):
            ary.append(n[j:j+i])
        if ary[0] == ary[1]:
            print("#", t+1, " ", len(ary[0]), sep="")
            break