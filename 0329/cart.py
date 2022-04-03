# 순열
def nPr(i, N, s):
    global minV

    if i == N:
        s += arr[p[N-1]][0]
        if minV > s:
            minV = s
    elif s >= minV:
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            nPr(i+1, N, s + arr[p[i-1]][p[i]])
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 99999
    p = [i for i in range(N)]
    nPr(1, N, 0)

    print(f'#{tc} {minV}')