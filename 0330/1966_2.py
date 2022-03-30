def partition2(arr, p, r):
    x = arr[r]
    i = p-1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick(arr, l, r):
    if l < r:
        s = partition2(arr, l, r)	#피벗 위치를 반환
        quick(arr, l, s-1)      # 피벗 왼쪽
        quick(arr, s+1, r)      # 피벗 오른쪽

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    quick(lst, 0, N-1)
    print(f'#{tc} ', end='')
    print(*lst)