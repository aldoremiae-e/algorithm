T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_num = 0
    min_num = 100000000000
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            cnt += arr[i+j]
        if cnt > max_num:
            max_num = cnt
        if cnt < min_num:
            min_num = cnt
    print(max_num - min_num)