def f(i, k, l, cnt):
    global minV
    if i == k:
        minV = min(cnt, minV)
        return
    if cnt >= minV:
        return
    else:
        if l > 0:   # 통과
            f(i+1, k, l-1, cnt)
        f(i+1, k, lst[i]-1, cnt+1)  # 교체
    return


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]      # 정류장 개수
    lst = [0] * (N+1)       # 배터리 용량
    minV = N
    for i in range(1, len(arr)):
        lst[i] = arr[i]
    f(2, N, lst[1] - 1, 0)

    print(f'#{tc} {minV}')