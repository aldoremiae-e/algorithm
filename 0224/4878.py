def start():
    for c in range(N):
        for r in range(N):
            if arr[c][r] == 2:
                return c, r
    return -1, -1

#di = [1, 0, -1, 0]
#dj = [0, 1, 0, -1]
def maze(i, j, N):
    # 스택사용
    stack = []
    visited = [[0] * N for _ in range(N)]
    while 1:
        # 방문했다면 1
        visited[i][j] = 1
        # 목적지라면
        if arr[i][j] == 3:
            return 1
        # 델타
        for di, dj in [[0,1], [1,0], [0,-1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 갈 수 있는 칸: 미로 내부, 벽이 아니고(통로, 도착칸), 방문X
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                # 현재 위치 스택에 저장 후 이동
                stack.append((i, j))
                i, j = ni, nj
                break
        # 갈 수 없다
        else:
            # 지워서 pop
            if stack:
                i, j = stack.pop()
            # 출발지로 돌아왔다? -> 실패
            else:
                break
    return 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    c, r = start()
    print(f'#{tc} {maze(c, r, N)}')




