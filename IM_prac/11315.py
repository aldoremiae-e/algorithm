dr = [1, 1, 0, -1]
dc = [0, 1, 1, 1]
def check():
    for r in range(N):
        for c in range(N):
            if arr[r][c] =='.':
                continue
            # 돌을 만났을 때, 기준점 = (r,c)
            # 다섯개냐?
            for i in range(4):
                nr, nc = r, c
                for _ in range(4):
                    nr = nr + dr[i]
                    nc = nc + dc[i]
                    if nr < 0 or nr >= N or nr < 0 or nc >= N or arr[nr][nc] == '.':
                        break
                else:
                    return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    # 8 방향 델타인데 시계방향으로 (3시) 0 1 2 3 4 5 6 7 8
    # 0 1 2 3 만 확인하면 됨

    N = int(input())
    arr = [input() for _ in range(N)]

    print(check())