# n, k = map(int, input().split())
# p = list(map(int, input().split()))
a = input()
number = ''
ary = []
for i in a:
    if i.isdigit():
        number = number + i
    if not i.isdigit():
        ary.append(number)
        ary.append(i)
        number = ''
ary.append(number)
# print(ary)

minary = []
plsary = []
flag = 0
for i in ary:
    if i == '-':
        flag = 1
        continue
    if i == '-' and flag == 1:
        flag = 0
        continue
    if flag == 1 and i != '+':
        minary.append(int(i))
        continue
    if i != '+':
        plsary.append(int(i))
print(sum(plsary)-sum(minary))


