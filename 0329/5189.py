def nPr(i, N, s):
    global minV

    if i == N:
        s += arr[p[N-1]][0]
        if minV > s:
            minV = s
    elif s >= minV:     # 굉장히 빨라짐
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i] #i번째 방문지 결정
            nPr(i+1, N, s+arr[p[i-1]][p[i]])
            p[i], p[j] = p[j], p[i]
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]
    minV = 999999
    nPr(1, N, 0)
    print(f'#{tc} {minV}')