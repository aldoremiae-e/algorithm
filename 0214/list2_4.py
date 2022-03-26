T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    row = 0
    col = -1
    num = 1
    while N > 0:
        for i in range(N):
            col += 1
            arr[row][col] = num
            num += 1
        N -= 1
        for j in range(N):
            row += 1
            arr[row][col] = num
            num += 1
        for i in range(N):
            col -= 1
            arr[row][col] = num
            num += 1
        N -= 1
        for j in range(N):
            row -= 1
            arr[row][col] = num
            num += 1
    print(f'#{tc}')
    print(arr)
    for i in arr:
        for j in i:
            print(j, end=' ')
        print('\n', end='')










