def BFS(i, j, N):
    q = []  # 큐 생성
    q.append((i, j))    # 큐에 시작점 추가
    v = [[0] * N for _ in range(N)]     # 방문
    v[i][j] = 1

    while q:
        # 디큐!!!!
        i, j = q.pop(0)
        if arr[i][j] == 3:
            return 1
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if (0 < ni <= N and 0 < nj <= N) and (arr[ni][nj] != 1 and v[ni][nj] == 0):
                q.append((ni, nj))
                v[ni][nj] = 1
    return 0

for _ in range(1, 10):
    tc = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]

    # find start
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                print(si,sj)
                break

    print(f'#{tc} {BFS(si, sj, N)}')