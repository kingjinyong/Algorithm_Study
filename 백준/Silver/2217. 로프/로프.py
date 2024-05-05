
n = int(input())
rope = [0] * 10001

for _ in range(n):
    rope[int(input())] += 1

result = 0
count = n

for i in range(1, 10001, 1):
    if rope[i] > 0:
        result = max(result, i*count)
        count -= rope[i]

print(result)