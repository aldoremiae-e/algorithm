def rot(arr, N):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]
    return new_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr_0 = [list(map(int, input().split())) for _ in range(N)]

    arr_1 = (rot(arr_0, N))
    arr_2 = (rot(arr_1, N))
    arr_3 = (rot(arr_2, N))
    print(f'#{tc}')
    for a1, a2, a3 in zip(arr_1, arr_2, arr_3):
        print(f'{"".join(map(str, a1))} {"".join(map(str, a2))} {"".join(map(str, a3))}')
