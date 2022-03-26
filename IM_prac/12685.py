'''
    [0,1]~[0,N-2]
    [1,0]~[N-2,0]
    [N-2,1]~[N-2,N-2]
    [1,N-1]~[N-2,N-1]
    '''


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            tot = 0
            for k in range(M):
                tot += arr[row+k][col+k]
                tot += arr[row+k][col+M-1-k]
            if M % 2:
                tot = tot - arr[row + M//2][col + M//2]

            if cnt < tot:
                cnt = tot
    print(f'#{tc} {cnt}')
