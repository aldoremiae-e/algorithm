def r_sum(N, arr):
    max_sum = 0
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += arr[i][j]
        if row_sum > max_sum:
            max_sum = row_sum
    return max_sum

def c_sum(N, arr):
    max_sum = 0
    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum += arr[i][j]
        if col_sum > max_sum:
            max_sum = col_sum
    return max_sum

def cr_sum(N,arr):
    crs_sum = 0
    for j in range(N):
        for i in range(N):
            if i == j:
                crs_sum += arr[i][j]
    return crs_sum

def cr_sum_r (N,arr):
    crs_sum_r = 0
    for j in range(N):
        for i in range(N):
            if i + j == N-1 :
                crs_sum_r += arr[i][j]
    return crs_sum_r


for tc in range(1, 11):
    T = int(input())
    n = 100
    lst = [list(map(int, input().split())) for _ in range(n)]

    lst2 =[r_sum(n, lst), c_sum(n, lst), cr_sum(n, lst), cr_sum_r(n, lst)]
    max_num = 0
    for i in lst2:
        if i > max_num:
            max_num = i
    print(f'#{T} {max_num}')
