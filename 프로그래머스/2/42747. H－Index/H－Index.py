def solution(citations):
    # 인용 순으로 논문을 정렬시켜서
    citations.sort()
    print(citations)
    # 0번부터 시작
    for i in range(len(citations)):
        # i 번째 논문의 인용 횟수(h)가 논문 개수 - i 즉, h편 이상일 경우 
        if citations[i] >= len(citations) - i:
            return len(citations) - i
        
    # 해당 되는 부분이 없을 경우
    return 0