T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    res = 1

    # 네모
    for i in range(0, len(arr), 3):
        for j in range(0, len(arr), 3):
            num =[1, 2, 3, 4, 5, 6, 7, 8, 9]
            for k in range(3):
                for m in range(3):
                    if arr[i+k][j+m] in num:
                        num[arr[i+k][j+m]-1] = 0
            for x in num:
                if x != 0:
                    res = 0

    # 가로
    for i in range(len(arr)):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if arr[i][j] in num:
                num[arr[i][j]-1] = 0
        for x in num:
            if x != 0:
                res = 0


    # 세로
    arr = list(map(list, zip(*arr)))

    for i in range(len(arr)):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if arr[i][j] in num:
                num[arr[i][j]-1] = 0
        for x in num:
            if x != 0:
                res = 0

    print(f'#{tc} {res}')
