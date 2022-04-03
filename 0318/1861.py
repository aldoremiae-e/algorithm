def BFS(si, sj):
    q = []
    q.append((si, sj))
    sol = []    # 방문번호 저장
    v[si][sj] = 1
    sol.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)
        # 방문조건 - 4방향, 방문
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + di, cj + dj
            if (0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0) and abs(arr[ci][cj]-arr[ni][nj]) == 1:
                q.append((ni, nj))
                v[ni][nj] = 1
                sol.append(arr[ni][nj])
    return min(sol), len(sol)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())    # 방 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    # 방문리스트 여기다가 작성
    num = N * N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:    # 시작점
                tn, tc = BFS(i, j)
                if cnt < tc or cnt == tc and num > tn:
                    cnt = tc
                    num = tn
    print(num, cnt)