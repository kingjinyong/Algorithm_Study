test = int(input())
for t in range(1, test+1):
    n = input()
    if n == n[::-1]:
        print('#', t, ' ', 1, sep="")
    else:
        print('#', t, ' ', 0, sep="")
