'''풍선팡'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(-arr[i][j], arr[i][j]+1):
                # 인덱스 오류 행, 열 나눠서 고려
                if 0 <= i + k < N:
                    # 파리 퇴치랑 동일
                    cnt += arr[i + k][j]
                if 0 <= j + k < M:
                    cnt += arr[i][j + k]
            cnt -= arr[i][j]
            if res < cnt:
                res = cnt
    print(f'#{tc} {res}')