T = int(input())
for tc in range(1, T+1):
    N = 10
    arr = list(map(int, input().split()))

    # 부분집합 만들기
    for i in range(1, 1 << N): # 공집합 제외
        tot = 0
        for j in range(N):
            if i & (1 << j):
                tot += arr[j]
        if tot == 0:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')