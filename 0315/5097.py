T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = arr[M % N]
    print(f'#{tc} {ans}')
    front = -1
    q = [0] * M

    for i in range(M):
        front += 1
        q[front] = arr[0]
        for k in range(N-1):
            arr[k] = arr[k+1]
        arr[N-1] = q[front]
    #print(f'#{tc} {arr[0]}')