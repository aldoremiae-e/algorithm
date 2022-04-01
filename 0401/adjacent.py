'''
V, E마지막 정점번호, 간선수
6 8
0 1 0 2 0 5 0 6 5 3 4 3 5 4 6 4 (출발 도착 순으로 주어진다)
'''
#DFS
def dfs(v, V):
    visited = [0] * (V + 1)
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, V+1):
        if adjM[v][w] == 1 and visited[w] == 0:
            dfs(w, V)

def dfs2(v, V):
    stack = [v] # 스택생성 + 시작정점 push
    visited = [0] * (V+1)
    visited[v] = 1  # 스택에 들어간애는 방문표시

    while stack:
        v = stack.pop()
        print(v, end=' ')
        for w in range(1, V+1):
            if adjM[v][w] == 1 and visited[w] == 0: # 인접하고 미방문
                stack.append(w)     # 갈림길 목록 - 나로부터 제일 가까운걸 꺼낼거야
                visited[w] = 1

def dfs3(v, V):
    stack = [v] # 스택생성 + 시작정점 push
    visited = [0] * (V+1)

    while stack:
        v = stack.pop()
        if visited[v] == 0:
            print(v, end=' ')
            visited[v] = 1
        for w in range(1, V+1):
            if adjM[v][w] == 1 and visited[w] == 0: # 인접하고 미방문
                stack.append(w)     # 갈림길 목록 - 나로부터 제일 가까운걸 꺼낼거야


def bfs(s, V):
    q = []
    visited = [0] * (V+1)
    q.append(s)
    visited[s] = 1
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for w in range(1, V+1):
            if adjM[v][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return
def bfs2(s, V):
    q = []  # 큐 생성
    visited = [0] * (V+1)   #방문
    q.append(s) # 시작점 인큐
    visited[s] = 1  #시작점 인큐방문
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for w in adjL[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V+1) for _ in range(V+1)]    # 인접행렬
adjL = [[] for _ in range(V+1)]     #인접리스트
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]   #n1: 출발 n2:도착
    adjM[n1][n2] = 1        # 방향성인 경우, 인접이면 1이다
    #adjM[n2][n1] = 1        # 무향성인 경우

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
    print(adjL)
#dfs(1, V)
#dfs2(1, V)
#dfs3(1, V)
bfs(1, V)
print()
bfs2(1, V)