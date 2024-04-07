# n, k = map(int, input().split())
# p = list(map(int, input().split()))

n = int(input())

length = list(map(int, input().split()))

price = list(map(int, input().split()))

# print(n, length, price)

oil = 0

for i in range(len(price) - 1):
    oil += length[i] * price[i]
    if price[i] < price[i+1]:
        price[i+1] = price[i]

print(oil)




# 1. 첫번째에서는 무조건 주유를 해야함
# 2. 만약 다음 도시의 주유값이 현재 머무른 도시보다 주유값이 비싸면 더 넣어야함.

