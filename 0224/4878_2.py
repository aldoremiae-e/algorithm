def start():
    for c in range(N):
        for r in range(N):
            if arr[c][r] == 2:
                return c, r
    return -1, -1
# 재귀
def maze2(i, j, N):

    visited[i][j] = 1

    if arr[i][j] == 3:
        return 1
    else:
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                if maze2(ni, nj, N):
                    return 1
        return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    c, r = start()
    print(f'#{tc} {maze2(c, r, N)}')
