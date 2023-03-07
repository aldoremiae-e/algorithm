T = int(input())
for tc in range(1, T+1):
    # N 연결지점 번호, E 도로개수
    N, E = map(int, input().split())
    # s e w
    arr = [list(map(int, input().split())) for _ in range(E)]
    # 방문 배열
    v = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            for k in range(E):
                s = arr[k][0]
                e = arr[k][1]
                v[s][e] = arr[k][2]

    for i in range(N+1):
        res = float('inf')
        for j in range(N+1):
