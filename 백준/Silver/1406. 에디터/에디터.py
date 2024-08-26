import sys

s = list(sys.stdin.readline().rstrip())
s2 = []
c = len(s)

test = int(sys.stdin.readline())
for t in range(test):
    a = list(sys.stdin.readline().split())

    if a[0] == 'P':
        s.append(a[1])
    elif a[0] == 'L':
        if s:
            s2.append(s.pop())
    elif a[0] == 'D':
        if s2:
            s.append(s2.pop())
    elif a[0] == 'B':
        if s:
            s.pop()
s.extend(reversed(s2))
print(''.join(s))