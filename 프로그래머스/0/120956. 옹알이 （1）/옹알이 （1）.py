import itertools
def solution(babbling):
    answer = 0
    spk = ['aya', 'ye', 'woo', 'ma']
    fj = []
    count = 0
    for i in range(1, 5):
        j = list(itertools.permutations(spk,i))
        jl = []
        for i in j:
            jl.append(list(i))
        for i in range(len(jl)):
            jl[i] = ''.join(jl[i])
        for ong in babbling:
            if ong in jl:
                count+=1
    print(count)
    return count
                
#     tj = list(itertools.permutations(spk, 2))
    # tjl = []
    # for i in tj:
    #     tjl.append(list(i))
    # for i in range(len(tjl)):
    #     tjl[i] = ''.join(tjl[i])
#     # print(tjl)
    
#     thj = list(itertools.permutations(spk, 3))
#     thjl = []
#     for i in thj:
#         thjl.append(list(i))
#     for i in range(len(thjl)):
#         thjl[i] = ''.join(thjl[i])
#     # print(thjl)    
    
#     fj = list(itertools.permutations(spk, 4))
#     fjl = []
#     for i in fj:
#         fjl.append(list(i))
#     for i in range(len(fjl)):
#         fjl[i] = ''.join(fjl[i])
#     # print(fjl)
    
#     print([tjl, thjl, fjl])