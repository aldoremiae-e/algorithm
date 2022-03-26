T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxV = 0
    #가로 먼저
    for i_row in range(N):
        # 유적물의 길이
        row_max = 0
        for j_row in range(M):
            # 현재 위치에 유적물이 있다면
            if arr[i_row][j_row] == 1:
                row_max += 1
            # 없다면 초기화
            else:
                row_max = 0
            if row_max > maxV:
                maxV = row_max
    #세로
    for j_col in range(M):
        col_max = 0
        for i_col in range(N):
            if arr[i_col][j_col] == 1:
                col_max += 1
            else:
                col_max = 0
            if col_max > maxV:
                maxV = col_max

    print(f'#{tc} {maxV}')

