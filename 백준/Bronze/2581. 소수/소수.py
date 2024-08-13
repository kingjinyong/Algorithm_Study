m = int(input())
n = int(input())

prime_number = []

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True

for i in range(m, n+1):
        if is_prime(i):
            prime_number.append(i)
if len(prime_number) == 0:
    print(-1)
else:
    print(sum(prime_number))
    print(min(prime_number))