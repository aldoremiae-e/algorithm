import sys
sys.stdin = open("14229.txt", "r")


def partition2(arr, p, r):
    x = arr[r]  # pivot
    i = p-1     # 피벗보다 작은 구간의 왼쪽 경계

    for j in range(p, r):   #피벗보다 큰 구간의 오른쪽 구간
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick(arr, l, r):
    if l < r:
        s = partition2(arr, l, r)  #피벗 위치를 반환
        quick(arr, l, s-1)      # 피벗 왼쪽
        quick(arr, s+1, r)      # 피벗 오른쪽


lst = list(map(int, input().split()))
N = 1000000
quick(lst, 0, N-1)
print(lst[500000])