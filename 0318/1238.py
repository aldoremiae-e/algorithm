def BFS(s):
    q = []  # 큐 생성
    q.append(s) # 시작점 인큐
    v = [0] * 101   # 방문
    v[s] = 1    # 시작점 방문
    sol = s     # 결과

    while q:
        c = q.pop(0)    # 디큐
        # 정답처리 : v의 값이 똑같이 크다면 번호가 큰 경우
        # 가장 나중에 연락받는 사람 : v값이 가장 큰 값일 것
        # v가 가장 큰 값 중 번호가 가장 큰 것
        if v[sol] < v[c] or v[sol] == v[c] and sol < c:
            sol = c
        # 정답 아닐때
        for j in range(1, 101):
            if adjM[c][j] and v[j] == 0:    #조건에 맞으면
                q.append(j) # 인큐
                v[j] = (v[c] + 1)   #방문점에 순서같이
    return sol
T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    adjM = [[0]*101 for _ in range(101)]
    for i in range(0, len(arr), 2):
        adjM[arr[i]][arr[i+1]] = 1
    print(f'#{tc} {BFS(S)}')