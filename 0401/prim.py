def prim1(r, V):
    MST = [0] * (V+1)
    key = [10000] * (V+1)   #가중치 최대값으로 초기화
    key[r] = 0  # 시작정점의 최대값
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i]==0 and key[i]<minV:   #key값이 최소
                u = i
                minV = key[i]
        MST[u] = 1  #정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점
        for v in range(V+1):
            if MST[0]

V, E = map(int, input().split())
adjM = [[0] * (V+1) for _ in range(V+1)]    # 인접행렬
#adjL = [[] for _ in range(V+1)]     #인접리스트
for i in range(E):
    n1, n2, w = map(int, input().split())  #n1: 출발 n2:도착
    adjM[n1][n2] = w        # 방향성인 경우, w 가중치
    adjM[n2][n1] = w        # 무향성인 경우

prim1(0, V)
