def solution(nums):
    dic = {}
    for p in nums:
        if p not in dic:
            dic[p] = 1
            
    return min(len(nums)//2, len(dic))