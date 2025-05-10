test = int(input())

def calculator(x_len, y_len, x_ary, y_ary):
    answer = 0
    for i in range(y_len - x_len + 1):
        temp_y_ary = y_ary[i:i + x_len]
        temp = 0
        for j in range(x_len):
            temp += x_ary[j] * temp_y_ary[j]
        answer = max(answer, temp)
    return answer


for t in range(1, test + 1):
    N, M = map(int, input().split())
    a_ary = list(map(int, input().split()))
    b_ary = list(map(int, input().split()))

    a_len = len(a_ary)
    b_len = len(b_ary)

    if a_len < b_len:
        print(f"#{t} {calculator(a_len, b_len, a_ary, b_ary)}")
    elif b_len < a_len:
        print(f"#{t} {calculator(b_len, a_len, b_ary, a_ary)}")
    else:
        print(f"#{t} {calculator(a_len, b_len, a_ary, b_ary)}")