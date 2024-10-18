a, b = map(int, input().split())

a_ary = list(map(int, input().split()))
b_ary = list(map(int, input().split()))

while b_ary:
    a_ary.append(b_ary.pop())
a_ary.sort()
print(*a_ary)