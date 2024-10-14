def solution(people, limit):
    answer = 0    
    people.sort()
    
    start = 0
    end = len(people) -1
    while start < end:
        if people[start] + people[end] <= limit:
            answer += 1
            start += 1
        end -= 1
    return len(people) - answer


# [70, 20, 80, 30]
# [20, 30, 70, 80]

# [80, 70, 30, 20]

