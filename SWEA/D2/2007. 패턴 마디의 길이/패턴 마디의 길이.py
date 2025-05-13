test = int(input())

for t in range(1, test + 1):
    ary = list(input())
    for i in range(1, 11):
        answer = ary[:i]
        if ary[i:i + len(list(answer))] == answer:
            print(f"#{t} {len(answer)}")
            break
