T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 가로
    for i in range(N):
        for j in range(N-M+1):
            check = 0
            for k in range(M//2):
                if arr[i][j+k] == arr[i][j+M-1-k]:
                    check += 1
            if check == M//2:
                print(f'#{tc}', end=' ')
                for idx in range(M):
                    print(arr[i][j+idx], end='')
                print()

    # 세로
    for i in range(N):
        for j in range(N-M+1):
            check = 0
            for k in range(M//2):
                if arr[j+k][i] == arr[j+M-1-k][i]:
                    check += 1
            if check == M//2:
                print(f'#{tc}', end=' ')
                for idx in range(M):
                    print(arr[j+idx][i], end='')
                print()

