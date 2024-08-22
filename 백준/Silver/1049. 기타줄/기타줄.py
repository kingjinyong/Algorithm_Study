n, m = map(int, input().split())
smin = 1001
pmin = 1001
for i in range(m):
    s, p = map(int, input().split())
    if smin > s:
        smin = s
    if pmin > p:
        pmin = p

min_package = smin

ans = 0
while n > 0:
    if n >= 6:
        min_single = pmin*6
        n -= 6
    else:
        min_single = pmin*n
        n -= n
    if min_single < min_package:
        ans += min_single
    else:
        ans += min_package
print(ans)