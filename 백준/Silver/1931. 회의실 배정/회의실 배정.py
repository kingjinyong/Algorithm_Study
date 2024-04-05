# n, k = map(int, input().split())
n = int(input())
ary = []

for i in range(n):
    n, k = map(int, input().split())
    ary.append([n, k])

ary = sorted(ary, key=lambda x: (x[1], x[0])) # 끝나는 시간으로 배열을 정렬해야함
# print(ary)
count = 0
end_point = 0
for new_start, new_end in ary: # 해당 인덱스의 시작시간과 종료시간 가져오기
    if end_point <= new_start:  # 회의가 종료된 시간이 앞으로 회의가 시작되는 시간 이하라면
        count += 1              # 회의 갯수 1 업 하고
        end_point = new_end     # 회의 종료 시간을 새로운 회의의 종료시간으로 설정
print(count)