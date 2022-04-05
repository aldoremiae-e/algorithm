def prim(r, V):
    mst = [0] * (V+1)
    key = [10000] * (V+1)   # 가중치 최대
    key[r] = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if mst[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        mst[u] = 1
        for v in range(V+1):
            if mst[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])
    return sum(key)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w
        adjM[n2][n1] = w
    ans = prim(0, V)
    print(f'#{tc} {ans}')