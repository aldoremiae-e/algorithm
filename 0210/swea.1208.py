def my_min(arr):
    min_num = arr[0]
    min_idx = 0
    for j in range(len(arr)):
        if arr[j] < min_num:
            min_num = arr[j]
            min_idx = j
    return min_idx


def my_max(arr):
    max_num = arr[0]
    max_idx = 0
    for j in range(len(arr)):
        if arr[j] > max_num:
            max_num = arr[j]
            max_idx = j
    return max_idx


for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    # 5 8 3 1 5 6 9 9 2 2 4
    for i in range(N):
        lst[my_min(lst)] += 1
        lst[my_max(lst)] -= 1

    print(f'#{tc} {lst[my_max(lst)] - lst[my_min(lst)]}')