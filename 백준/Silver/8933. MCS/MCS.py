test = int(input())

for _ in range(test):
    k, dna = map(str, input().split())
    k = int(k)
    dic = {}
    
    # 초기 윈도우에서의 문자 개수를 계산
    count = {'A': 0, 'G': 0, 'C': 0, 'T': 0}
    for char in dna[:k]:
        count[char] += 1
    
    # 첫 윈도우의 상태 저장
    s = str(count['A']) + str(count['G']) + str(count['C']) + str(count['T'])
    dic[s] = 1

    # 슬라이딩 윈도우 시작
    for end in range(k, len(dna)):
        # 새로운 문자를 추가하고, 윈도우에서 벗어난 문자를 제거
        count[dna[end]] += 1
        count[dna[end - k]] -= 1
        
        # 현재 윈도우의 상태를 문자열로 생성
        s = str(count['A']) + str(count['G']) + str(count['C']) + str(count['T'])
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

    print(max(dic.values()))
