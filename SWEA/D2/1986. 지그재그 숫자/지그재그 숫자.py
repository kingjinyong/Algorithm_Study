test = int(input())
for t in range(test):
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            result += i
        else:
            result -= i
    print('#', t+1, ' ', result, sep='')