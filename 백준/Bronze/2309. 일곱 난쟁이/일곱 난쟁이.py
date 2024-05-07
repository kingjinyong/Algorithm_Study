ary = []
for _ in range(9):
    ary.append(int(input()))
ary.sort()
total_ary = sum(ary)

for i in range(len(ary)):
    for j in range(i + 1, len(ary)):
        if total_ary - ary[i] - ary[j] == 100:
            for k in range(len(ary)):
                if k == i or k == j:
                    pass
                else:
                    print(ary[k])
            exit()
