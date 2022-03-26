for tc in range(0, 10):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    row_big = 0
    col_big = 0
    down_big = 0
    up_big = 0
    big_big = 0
    row_sum = [0] * 100
    col_sum = [0] * 100
    big = [0] * 4
    for i in range(100):
        for j in range(100):
            row_sum[i] += arr[i][j]
        if row_sum[i] > row_big:
            row_big = row_sum[i]
            big[0] = row_big

    for j in range(100):
        for i in range(100):
            col_sum[j] += arr[i][j]
        if col_sum[j] > col_big:
            col_big = col_sum[j]
            big[1] = col_big

    for i in range(100):
        down_big += arr[i][i]
        big[2] = down_big

    for i in range(100):
        up_big += arr[i][99 - i]
        big[3] = up_big

    for i in range(4):
        if big[i] > big_big:
            big_big = big[i]

    print(f'#{N} {big_big}')