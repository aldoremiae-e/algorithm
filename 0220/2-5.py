for tc in range(1,11):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    row = 0
    col = -1
    num = 1
    trans = 1
    while N > 0:
        for i in range(N):
            col += trans
            arr[row][col] = num
            num += 1
        N -= 1
        for j in range(N):
            row += trans
            arr[row][col] = num
            num += 1
        trans *= -1

    print(f'#{tc}')
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()
