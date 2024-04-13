n = int(input())
ary = [0, 1]

for i in range(2, n+1):
    ary.append(ary[i-1] + ary[i-2])
print(ary[-1])
