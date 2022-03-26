def BFS(i, j, N): # 시작점
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        i, j = queue.pop(0)
        if arr[i][j] == 3:
            return visited[i][j] - 2
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if (0 <= ni <N and 0 <= nj < N) and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                queue.append((ni, nj))
                # count 따로 하지 않고 개수를 만듬
                visited[ni][nj] = visited[i][j] + 1
    return 0 # 도착못했을 떄

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # 시작점 만들기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
    print(f'#{tc} {BFS(si, sj, N)}')