def BFS(s):
    q = []
    visited = [0] * 101

    q.append(s)
    visited[s] = 1
    sol = s

    while q: # q에만 있을 떄만
        c = q.pop(0)
        # 조건
        if visited[sol] < visited[c] or visited[sol] == visited[c] and sol < c:
            sol = c

        for j in range(1, 101):
            if adj[c][j] and visited[j] == 0:
                q.append(j)
                visited[j] = visited[c] + 1
        # return c 마지막 pop하는 값을 확인
    return sol

T = 1
for tc in range(1, T+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[0]*101 for _ in range(101)]

    for i in range(0, len(lst), 2):
        adj[lst[i]][lst[i+1]] = 1
    ans = BFS(S)
    print(f'#{tc} {ans}')