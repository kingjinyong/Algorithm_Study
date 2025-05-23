test = int(input())

for t in range(1, test + 1):
    bit = input()
    p = '0'
    ans = 0
    for i in bit:
        if p != i:
            ans += 1
            p = i
    print(f"#{t} {ans}")
