''' 토글
0 -> 1, 1 -> 0
N -> 행,열수
M ->
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, (input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    all_t = 1
    cnt = 0
    for k in range(1, M+1):
        # 전체 토글 될 경우가 제일 우선시 되어야함
        if (M % k == 0) or (M == k):
            all_t *= -1
        else:
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if  (i + j == k) or ((i + j) % k == 0):
                        if arr[i - 1][j - 1] == 1:
                            arr[i - 1][j - 1] = 0
                        else:
                            arr[i - 1][j - 1] = 1
    if all_t == 1:
        for i in range(1, N+1):
            for j in range(1, N+1):
                if arr[i-1][j-1] == 1:
                    cnt += 1
    elif all_t == -1:
        for i in range(1, N+1):
            for j in range(1, N+1):
                if arr[i-1][j-1] == 0:
                    cnt += 1
    print(f'#{tc} {cnt}')



