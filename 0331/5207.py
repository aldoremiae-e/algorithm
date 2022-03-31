def binarySearch(arr, low, high, key):
    global cnt, check
    if low > high:
        return 0
    else:
        mid = (low + high) // 2
        if arr[mid] == key:
            cnt += 1
            return
        elif arr[mid] > key:
            if check == 1:
                return
            check = 1
            return binarySearch(arr, low, mid-1, key)
        else:
            if check == -1:
                return
            check = -1
            return binarySearch(arr, mid+1, high, key)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lsta = list(map(int, input().split()))
    lstb = list(map(int, input().split()))
    cnt = 0
    lsta.sort()
    lstb.sort()
    for x in lstb:
        check = 0
        binarySearch(lsta, 0, N-1, x)
    print(f'#{tc} {cnt}')