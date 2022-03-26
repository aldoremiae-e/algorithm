T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    for i in range(N):
        cnt = 0
        for j in range(i,i+M):
            if j < N :
                cnt += arr[i][j]
        if max_num < cnt:
            max_num = cnt
    print(f'#{tc} {max_num}')
