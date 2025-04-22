from collections import deque
test = int(input())

for t in range(test):
    dic = {}
    ary = list(input())
    ary_2 = list(input())
    for i in ary:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # print(dic)
    # print(ary)

    m = -1

    for i in dic.keys():
        m = max(ary_2.count(i), m)


    print("#", end="")
    print(t+1, m)