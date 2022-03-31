def part(arr, li ,ri):
    p = arr[li]
    i, j = li, ri
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]
    arr[li], arr[j] = arr[j], arr[li]
    return j

def quick(arr, li ,ri):
    if li < ri:
        pivot = part(arr, li, ri)   # 피벗
        quick(arr, li, pivot-1)
        quick(arr, pivot+1, ri)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    quick(lst, 0, N-1)
    print(f'#{tc} {lst[N//2]}')
