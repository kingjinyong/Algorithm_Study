test = int(input())

dic = {}
r_dic = {}

i = 1
j = 1

for n in range(1, 50000):
    dic[(i, j)] = n
    r_dic[n] = (i, j)
    i -= 1
    j += 1
    if i < 1:
        i = j
        j = 1

for t in range(1, test+1):
    p, q = map(int, input().split())
    pi, pj = r_dic[p]
    qi, qj = r_dic[q]

    ans = dic[(pi + qi, pj + qj)]
    print(f"#{t} {ans}")
