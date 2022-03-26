T = int(input())
for tc in range(1, T+1):
    # 20 * N
    N = (int(input())) // 10
    arr = [1 for _ in range(N+1)]
    print(N)
    for i in range(2, N+1):
        arr[i] = arr[i-1] + (arr[i-2] * 2)
    print(f'#{tc} {arr[-1]}')
