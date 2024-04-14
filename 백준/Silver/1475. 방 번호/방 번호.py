number = input()
ary = [0] * 10

for i in range(len(number)):
    n = int(number[i])
    if n == 6 or n == 9:
        if ary[6] >= ary[9]:
            ary[9] += 1
        else:
            ary[6] += 1
    else:
        ary[n] += 1
print(max(ary))