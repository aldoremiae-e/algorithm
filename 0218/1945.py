T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0 for _ in range(5)]
    lst = [2, 3, 5, 7, 11]

    while N % 2 == 0:
        N = N//2
        arr[0] += 1
    while N % 3 == 0:
        N = N//3
        arr[1] += 1
    while N % 5 == 0:
        N = N//5
        arr[2] += 1
    while N % 7 == 0:
        N = N//7
        arr[3] += 1
    while N % 11 == 0:
        N = N//11
        arr[4] += 1
    print(f'#{tc}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()