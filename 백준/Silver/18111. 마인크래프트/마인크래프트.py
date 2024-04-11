n, m, b = map(int, input().split())  # 지형의 크기와 소유한 블록 개수를 입력받음
ary = []  # 지형 정보를 저장할 배열
height_info = dict()  # 각 높이의 개수를 저장할 사전

# 지형 정보를 입력받아 이차원 배열에 저장
for i in range(n):
    ary.append(list(map(int, input().split())))

# 각 높이별 블록의 개수를 세어 사전에 저장
for i in ary:
    for j in i:
        if j not in height_info:
            height_info[j] = 1
        else:
            height_info[j] += 1

height_info = list(height_info.items())  # 사전을 리스트 형태로 변환하여 높이와 개수를 쌍으로 저장

time_list = []  # 각 높이에 대한 걸리는 시간을 저장할 리스트

# 높이가 0부터 256까지 변화할 때 걸리는 시간을 계산
for i in range(257):
    # 해당 높이보다 낮은 높이에 있는 블록과 높은 높이에 있는 블록을 구분하여 계산
    under = [(key, val) for key, val in height_info if key < i and val != 0]
    over = [(key, val) for key, val in height_info if key > i and val != 0]
    
    time, block = 0, 0  # 현재 높이에서 걸리는 시간과 남은 블록의 개수를 초기화
    block += b  # 소유한 블록의 개수를 블록에 추가

    # 높은 높이에 있는 블록을 현재 높이로 옮길 때 걸리는 시간 계산
    for height, count in over:
        time += 2 * (height - i) * count  # (높이 차이 * 블록 개수 * 2)
        block += (height - i) * count  # 블록을 옮긴 후 블록 개수 업데이트
        
    # 낮은 높이에 있는 블록을 현재 높이로 옮길 때 걸리는 시간 계산
    for height, count in under:
        time += (i - height) * count  # (높이 차이 * 블록 개수)
        block -= (i - height) * count  # 블록을 옮긴 후 블록 개수 업데이트

    # 블록이 부족하면 반복 종료
    if block < 0:
        break
    
    # 해당 높이에서 걸리는 시간을 리스트에 추가
    time_list.append(time)

# 걸리는 시간이 가장 짧은 경우와 그 때의 최종 높이를 찾음
max_height_idx = [idx for idx, t in enumerate(time_list) if t == min(time_list)]
max_height = max(max_height_idx)  # 걸리는 시간이 가장 짧은 경우의 최종 높이
min_time = min(time_list)  # 최소 걸리는 시간

# 결과 출력
print(min_time, max_height)
