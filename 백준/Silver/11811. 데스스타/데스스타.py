def solve():
    N = int(input())  # 행렬의 크기 N
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = [0] * N  # 결과 수열을 저장할 리스트

    for i in range(N):
        # 각 i에 대해 a[i]를 구해야 함
        # a[i]는 m[i][j]의 값들을 통해 추정 가능
        result[i] = matrix[i][0]  # 초기값을 일단 첫 번째 열 값으로 설정
        for j in range(1, N):
            result[i] |= matrix[i][j]  # 비트 OR로 해당 행의 모든 값들로 추정
    
    # 결과 출력
    print(' '.join(map(str, result)))

# 예제 실행
solve()