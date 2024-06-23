test = int(input())
for t in range(test):
    q, w, e, r = map(int, input().split())

    minute = w + r
    hour = (q + e + (w + r) // 60) % 12
    if hour == 0:
        hour = 12
    print('#', t+1, ' ', hour, ' ', minute % 60, sep='')