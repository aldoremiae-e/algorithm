#maze

def BFS(i, j):
    q = []
    q.append((i, j))
    # 방문한 곳 표시 할 것
    v = [[0]*16 for _ in range(16)]
    v[i][j] = 1

    while q:
        i, j = q.pop(0)
        # 미로 도착지점
        if maze[i][j] == 3:
            return 1
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            # 인덱스 오류, 벽이 아니고 방문한 곳이 아닐 때
            if (0 <= ni < 16 and 0 <= nj < 16) and (maze[ni][nj] != 1 and v[ni][nj] == 0):
                q.append((ni, nj))
                v[ni][nj] = 1
    # 미로도착 불가
    return 0

for _ in range(1, 1+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # find start
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                si, sj = i, j
                break

    print(f'#{tc} {BFS(si, sj)}')