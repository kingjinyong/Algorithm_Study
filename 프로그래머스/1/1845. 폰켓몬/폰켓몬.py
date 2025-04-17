def solution(nums):
    dic = {}
    for p in nums:
        if p not in dic:
            dic[p] = 1
            
    if len(nums)//2 > len(dic):
        return len(dic)
    else:
        return len(nums)//2