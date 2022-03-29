def f(n, i, j, s):  # n : 배열크기, 처음행, 처음열, 처음값
    global minV
    if i == n-1 and j == n-1 and minV > s:
        minV = s
    if minV <= s:
        return
    else:
        for di, dj in [[1, 0], [0, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                f(n, ni, nj, s + arr[ni][nj])   # 처음 값에 값 더해서 움직일 것임

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 99999
    f(N, 0, 0, arr[0][0])
    print(f'#{tc} {minV}')