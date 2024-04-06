# n, k = map(int, input().split())
n = int(input())
p = []
p = list(map(int, input().split()))
p.sort()

answer = 0
for i in range(len(p)):
    for j in range(i+1):
        answer += p[j]
print(answer)