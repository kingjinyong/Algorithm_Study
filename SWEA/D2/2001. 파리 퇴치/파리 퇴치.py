test = int(input())
for t in range(1, test+1):
    area = []

    n, m = map(int, input().split())
    for i in range(n):
        area.append(list(map(int, input().split())))

    max = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            temp = 0
            for k in range(m):
                for l in range(m):
                    temp += area[i + k][j + l]
            if temp > max:
                max = temp
    print('#', t, ' ', max, sep='')

    # 5 2 -> i를 3까지 가능
    # 5 3 -> i를 2까지 가능