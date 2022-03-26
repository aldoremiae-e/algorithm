T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))


    # 버블정렬
    # 각 원소 i의 오른쪽에 있는 더 작은 원소의 개수
    cnt = [0]*N                     # 0*(N-1)
    for i in range(N-1):            # [N-2]까지
        for j in range(i+1, N):     # i 의 오른쪽 원소
            if arr[i] > arr[j]:
                cnt[i] += 1

    #최댓값 찾기
    maxV =cnt[0]
    for i in range(1, N):
        if maxV < cnt[i]:
            maxV = cnt[i]

    print(f'#{tc} {maxV}')