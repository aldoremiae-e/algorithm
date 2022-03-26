T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                continue
            elif arr[i][j] == 'A':
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 'H' and 0 <= ni < N and 0 <= nj < N:
                        arr[ni][nj] = 'X'
            elif arr[i][j] == 'B':
                for di, dj in [[2, 0], [1, 0], [0, 2], [0, 1], [-2, 0], [-1, 0], [0, -2], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 'H' and 0 <= ni < N and 0 <= nj < N:
                        arr[ni][nj] = 'X'
            elif arr[i][j] == 'C':
                for di, dj in [[3, 0], [2, 0], [1, 0], [0, 3], [0, 2], [0, 1], [-3, 0], [-2, 0], [-1, 0], [0, -3], [0, -2], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 'H' and 0 <= ni < N and 0 <= nj < N:
                        arr[ni][nj] = 'X'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')