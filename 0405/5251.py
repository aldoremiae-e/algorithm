T = int(input())
for tc in range(1, T+1):
    INF = 9999
    N, E = map(int, input().split())
    adjM = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        adjM[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w

    #다익스트라
    d = [adjM[0][i] for i in range(N+1)]    #출발점 0
    # d = adjM[0][:]
    u = [0] * (N+1)
    u[0] = 1
    for _ in range(N):  # N+1개의 정점 중 출발을 제외한 N개
        minV = INF
        w = 0
        for i in range(N+1):
            if u[i] == 0 and minV > d[i]:
                minV = d[i]
                w = i
        u[w] = 1
        #w에 인접인 정점 v에 대해 출발에서의 도착비용 d[v] 갱신시도
        for v in range(N+1):
            if 0 < adjM[w][v] < INF:    # v가 w에 인접
                d[v] = min(d[v], d[w]+adjM[w][v])   # 기존 비융, w를 거쳐서 v로 가는 비용
    print(f'#{tc} {d[N]}')
