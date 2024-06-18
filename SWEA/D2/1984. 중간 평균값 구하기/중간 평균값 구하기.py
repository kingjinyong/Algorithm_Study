test = int(input())

for t in range(test):
    ary = list(map(int, input().split()))
    maxn = max(ary)
    minn = min(ary)
    ary.remove(maxn)
    ary.remove(minn)
    print('#', t+1, ' ', round(sum(ary) / len(ary)), sep='')
