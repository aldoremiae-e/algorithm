'''델타탐색을 이용한 2차원 배열'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    total = 0
    # 인덱스 주의
    for i in range(N):
        for j in range(N):
            for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    total += abs(arr[ni][nj]-arr[i][j])
    print(total)

