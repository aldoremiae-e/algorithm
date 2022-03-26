'''우주선'''
T = int(input())
for tc in range(1, T+1):
    # N 행 M 열
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    tot = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[i][j] > arr[ni][nj]:
                        cnt += 1
            if cnt >= 4:
                tot += 1
    print(f'#{tc} {tot}')