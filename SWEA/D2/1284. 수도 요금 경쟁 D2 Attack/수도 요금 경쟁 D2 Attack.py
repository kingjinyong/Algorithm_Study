test = int(input())

for t in range(1, test + 1):
    p, q, r, s, w = map(int, input().split())

    company_a = p*w
    company_b = q

    if w > r:
        company_b += (w-r)*s

    print(f"#{t} {min(company_a, company_b)}")
