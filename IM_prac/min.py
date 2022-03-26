T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = 0
    for idx in range(1, N):
        if arr[idx] < arr[min_num]:
            min_num = idx
    print(f'#{tc} {min_num+1}')
