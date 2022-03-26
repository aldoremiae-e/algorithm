T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 나보다 같거나 높은 칸이 있으면 낙차 정지
    # 나보다 작은 칸이 몇개나 있는가? -> 낙차 높이일것
    # 개수중에 가장 큰애
    max_num = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
            if cnt > max_num:
                max_num = cnt
    print(f'#{tc} {max_num}')
