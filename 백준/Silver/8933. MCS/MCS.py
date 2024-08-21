test = int(input())
for t in range(test):
    k, w = map(str, input().split())
    k = int(k)
    left = 0
    right = k
    dic = {}
    while right <= len(w):
        ary2 = w[left:right]
        s = str(ary2.count("A")) + str(ary2.count("G")) + str(ary2.count("C")) + str(ary2.count("T"))
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
        left += 1
        right += 1
    print(max(dic.values()))