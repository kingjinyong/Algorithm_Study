def solution(genres, plays):
    hash_1 = {}
    hash_2 = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        hash_1[genre] = hash_1.get(genre, []) + [(play, i)]
        hash_2[genre] = hash_2.get(genre, 0) + play
        
    print(hash_1)
    print(hash_2)
    
    hash_2_sort = sorted(hash_2.items(), key = lambda x : -x[1])
    print(hash_2_sort)
    
    answer = []
    for genre, _ in hash_2_sort:
        hash_1[genre] = sorted(hash_1[genre], key = lambda x : (-x[0], x[1]))
        answer.extend([i for g, i in hash_1[genre][:2]])
    print(answer)

    return answer
    
    
    