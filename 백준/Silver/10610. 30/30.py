n = input()

if "0" not in n: # 10의 배수이려면 0이 있어야하는데 없으면 -1 출력
    print(-1)

else:
    num_sum = 0
    for i in range(len(n)):
        num_sum += int(n[i])

    if num_sum % 3 != 0: # 3의 배수가 아니라면? -1 출력
        print(-1)
    # 모든 조건이 충족 되었으니
    else:
        sorted_num = sorted(n, reverse=True) # 내림차순 정렬하고 
        answer = "".join(sorted_num)
        print(answer) # 출력