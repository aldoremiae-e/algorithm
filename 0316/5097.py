def bfs(i, j): # 미로 도착여부 확인
    visited = [[0]*16 for _ in range(16)]# visited 생성
    q = [] # 큐 생성
    q.append((i, j)) # 시작점 인큐
    visited[i][j] = 1 # 시작점 방문표시

    while q: # 큐가 비어있지않으면
        i, j = q.pop(0)  # 디큐
        if maze[i][j] == '3':  # 도착하면
            return 1
        for di, dj in [[0,1], [1,0], [0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            # 항상 벽으로 둘러쌓인 미로의 경우 인덱스에러 생략 가능
            if maze[ni][nj] != '1' and visited[ni][nj] == 0: # 벽이 아니고 방문한 적이 없으면
                q.append((ni, nj))
                visited[ni][nj] = 1 # 각 칸에 갔는지 안갔는지만 알 수 있다. (도착여부만)
                # 최단거리 정보를 얻으려면 visited[i][j] + 1이런 식

    return 0


for _ in range(10):
    tc = int(input())
    maze = [input() for _ in range(16)]
    sti = -1
    stj = -1
    for i in range(16): # 출발 위치 찾기
        for j in range(16):
            if maze[i][j] == '2': # 문자열로 저장
                sti, stj = i, j
                break
        if sti != -1: #벽
            break
    print(f'#{tc} {bfs(sti, stj)}')