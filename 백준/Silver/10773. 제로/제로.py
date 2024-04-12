
n = int(input())
ary = []

for i in range(n):
    ary.append(int(input()))
    if ary[-1] == 0:
        ary.pop()
        ary.pop()
print(sum(ary))