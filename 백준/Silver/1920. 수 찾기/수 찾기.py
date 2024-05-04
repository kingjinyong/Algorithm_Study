
n = int(input())
arr_n = list(map(int, input().split()))
arr_n.sort()

m = int(input())
arr_m = list(map(int, input().split()))

for m in arr_m:
    left = 0            # 왼쪽 포인터
    right = n - 1       # 오른쪽 포인터

    while left <= right:     # 왼, 오 포인터가 같아지거나 엇갈리는 순간 반복문 종료
        mid = (left + right) // 2       # 가운데 값 만들어주기
        if m > arr_n[mid]:              # arr_n의 중간 인덱스 요소 값보다 크다면 ?
            left = mid + 1              # 왼쪽 포인터의 인덱스 값을 중간 인덱스 값 보다 1 크게 설정
        elif m < arr_n[mid]:            # 반대로
            right = mid - 1             # 반대로
        else:                           # m이 중간 인덱스 요소 값과 같은 경우면?
            left = mid                  # 왼쪽 포인터 = 중간 인덱스값
            right = mid                 # 오른쪽 포인터 = 중간 인덱스값
            break                       # 반복문 탈출

    if left == mid and right == mid:    # 결국 두 포인터가 중간 인덱스 값과 같다면 1 출력
        print(1)
    else:
        print(0)