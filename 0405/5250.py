def f(N):
    v[0][0] = 0  # 출발위치 방문
    q = [(0, 0)]
    while q:    #비용이 갱신되는 정점
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                diff = arr[ni][nj] - arr[i][j] if arr[ni][nj] > arr[i][j] else 0
                if v[ni][nj] > v[i][j] + diff + 1:
                    v[ni][nj] = v[i][j] + diff + 1
                    q.append((ni, nj))
    return v[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[99999] * N for _ in range(N)]  # 비융기록
    ans = f(N)
    print(f'#{tc} {ans}')