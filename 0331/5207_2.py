def binarySearch(n, arr, key):
    global cnt
    low = 0
    high = n - 1
    check = 0   #구간 선택
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            cnt += 1
            return
        elif arr[mid] > key:
            if check == 1: break # 오른쪽 - 오른쪽
            check = 1   # 오른쪽 구간 선택해라
            high = mid - 1
        else:
            if check == -1 : break  #왼쪽 - 왼쪽
            check = -1  # 왼쪽구간 선택해라
            low = mid + 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lsta = list(map(int, input().split()))
    lstb = list(map(int, input().split()))
    cnt = 0
    lsta.sort()
    lstb.sort()
    for x in lstb:
        binarySearch(N, lsta, x)
    print(f'#{tc} {cnt}')