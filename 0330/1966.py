def partition1(arr, l, r):  # 피벗 위치 찾기1
    p = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j  # 피벗의 위치를 고정시키고 반환

def quick(arr, l, r):
    if l < r:
        s = partition1(arr, l, r)	#피벗 위치를 반환
        quick(arr, l, s-1)      # 피벗 왼쪽
        quick(arr, s+1, r)      # 피벗 오른쪽

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    quick(lst, 0, N-1)
    print(f'#{tc} ', end='')
    print(*lst)

