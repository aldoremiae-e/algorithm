
'''
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 2

'''
# 호인영님 코드 최고
for tc in range(10):
    T = int(input())
    # 이중배열 받기, 앞뒤에 0 붙여서 인덱스 오류해결
    arr = [[0] + list(map(int, input().split())) + [0] for i in range(100)]
    # 도착지점
    for i in range(102):
        if arr[99][i] == 2:
            row = i
    col = 99
    # 아래에서 위로 탐색, 시작지점은 row = 1
    while col > 0:
        # 오른쪽이 1이면
        if arr[col][row + 1] == 1:
            # 수평은 지나간 자리 지움
            arr[col][row] = 0
            # 왼쪽으로 이동
            row += 1
        # 위쪽이 1이면
        elif arr[col][row - 1] == 1:
            arr[col][row] = 0
            # 오른쪽으로 이동
            row -= 1
        # 위쪽이 1이면
        elif arr[col - 1][row] == 1:
            #위쪽으로 이동
            col -= 1

    print(f'#{T} {row - 1}')