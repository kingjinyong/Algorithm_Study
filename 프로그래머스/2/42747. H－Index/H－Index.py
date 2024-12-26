def solution(citations):
    citations.sort()
    print(citations)

    for i in range(len(citations)):
        print(citations[i])
        if citations[i] >= len(citations) - i:
            print(citations[i], len(citations) - i)
            return len(citations) - i

    return 0

print(solution([3, 0, 6, 1, 5]))
