a = int(input())
floor = []
for i in range(a):
    floor.append(int(input()))

def solution(n, floor_list):

    dp = [0]*301
    lists = [0]*301

    for i in range(1, n+1):
        lists[i] = floor_list[i-1]
    dp[1] = lists[1]
    dp[2] = lists[2]+lists[1]
    dp[3] = max(lists[3]+lists[2], lists[3]+lists[1])

    for i in range(4, n+1):
        dp[i] = max(dp[i-3]+lists[i]+lists[i-1], dp[i-2]+lists[i])
        # print(dp)
    
    return dp[a]


print(solution(a, floor))