'''
배열 사각영역들의 합
이차배열 안에서 일정한 영역을 탐색
'''

T = int(input())
for tc in range(1, T+1):
    # N : 큰네모 M : 작은네모 개수
    N, M = map(int, input().split())
    big = [list(map(int, input().split())) for _ in range(N)]

    # 좌상단 위치와 변의 길이  (1,0), 2
    cdn = []
    tot = 0
    for _ in range(M):
        row, col, length = map(int, input().split())
        # 중복 어케 빼지?
        for i in range(row, row+length):
            for j in range(col, col+length):
                if 0 <= i < N and 0 <= j < N:
                    if (i, j) not in cdn:
                        cdn.append((i, j))
                        tot += big[i][j]
    print(f'#{tc} {tot}')