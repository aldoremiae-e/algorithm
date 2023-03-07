def my_dfs(i, j):
    # q : 현재좌표
    q = [[i, j]]
    while q:
        print(q)
        i, j = q.pop(0)
        for di, dj in [[0,1], [1,0], [-1,0],[0,-1]]:
            ni, nj = i + di, j + dj
            # 칸 내에 있는 좌표
            if 0 <= ni < N and 0  <= nj < N:
                # 추가비용
                if arr[ni][nj] > arr[i][j]:
                    diff = arr[ni][nj] - arr[i][j]
                else:
                    diff = 0
                # 최소비용을 방문배열에 입력
                if v[ni][nj] > (v[i][j] + diff + 1):
                    v[ni][nj] = v[i][j] + diff + 1
                    q.append((ni, nj))
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[100000] * N for _ in range(N)] # 방문 배열
    v[0][0] = 0 # 출발위치 방문
    my_dfs(0,0)
    print('#{} {}'.format(tc, v[N-1][N-1]))
