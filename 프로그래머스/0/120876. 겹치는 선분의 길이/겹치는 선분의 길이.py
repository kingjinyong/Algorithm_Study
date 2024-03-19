def solution(lines):
    answer = 0
    # -100 ~ 100까지의 범위를 리스트로 표현하기 위해 0~200범위의 리스트를 생성해준다
    count = [0 for _ in range(200)]
    for line in lines:
        for i in range(line[0], line[1]): # 선분이 위치한 범위를 리스트에 1을 추가해주어 해당 자리에 위치할 때 마다 1을 올려준다
            count[i + 100] += 1
    # 선분이 2개이상 겹치는 곳이라면 count해서 answer에 더해주기
    answer += count.count(2)
    answer += count.count(3)
    return answer
