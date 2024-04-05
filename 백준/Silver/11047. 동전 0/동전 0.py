n, k = map(int, input().split())
ary = []
for i in range(n):
    ary.append(int(input()))
# print(ary)
ary = sorted(ary, reverse=True)
# print(ary)
count = 0
for i in ary:
    if i <= k:
        count += k//i
        k %= i

    if k == 0:
        break
print(count)