
n = int(input())
lope = []
for i in range(n):
    lope.append(int(input()))

lope = sorted(lope, reverse=True)
max_w = 0

while lope:
    length = len(lope)
    w = lope.pop() * length
    if w > max_w:
        max_w = w
print(max_w)