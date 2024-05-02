n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
result = []

for i in a:
    bm = max(b)
    result.append(i * bm)
    b.remove(bm)
print(sum(result))