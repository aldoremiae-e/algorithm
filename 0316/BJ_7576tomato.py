def bfs(N, M):
    #visited
    visited = [[0]*M for _ in range(N)]
    #queue
    q = [0] * (N*M)
    front = -1
    rear = -1
    cnt = 0 # 안익은 토마토 개수
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
            # 추가
            #q.appemnd((i, j))
                rear += 1
                q[rear] = (i, j)
            # 시작점 인큐 표시
                visited[i][j] = 1
            elif tomato[i][j] == 0:
                cnt += 1
    # 안익은 토마토만 주어진 경우
    if cnt == 0 and len(q) > 0:
        return 0
    # 큐가 비어있지 않으면 (익은 토마토가 있는 경우)
    while front != rear:
        front += 1
        i, j = q[front] # 익은 토마토
        # visit(i, j)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 에러 방지 + 인접한 칸에 안익은 토마토 있으면
            if 0<=ni<N and 0<=nj<M and tomato[ni][nj]==0 and visited[ni][nj]==0:
                rear += 1
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j] + 1
    maxV = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                # 안익은 경우
                if visited[i][j] == 0:
                    return -1
                # 익은경우 날짜 비교
                elif maxV < visited[i][j]:
                    maxV = visited[i][j]
    return maxV-1

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
print(bfs(N, M))