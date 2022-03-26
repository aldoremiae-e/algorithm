'''
5
13101
10101
10101
10101
10021
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(arr)
    # 1 : 벽 , 0 : 통로 2 : 출발, 3 : 도착
    # 도착 지점, 출발 지점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            if arr[i][j] == 3:
                ei, ej = i, j

