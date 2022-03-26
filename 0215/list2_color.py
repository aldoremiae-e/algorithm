T = int(input())
for tc in range(T):
    N = int(input())
    # N개의 박스 인풋
    box = [0]*N
    for idx in range(N):
        box[idx] = list(map(int, input().split()))
    blank = [[0]*10 for _ in range(10)]
    cnt = 0
    # 인덱스 0, 2 : 행 1, 3 : 열 , color 1, 2
    for k in range(N):
        # 좌표 설정
        ni, nj, mi, mj = box[k][0], box[k][1], box[k][2], box[k][3]
        for i in range(ni, mi+1):
            for j in range(nj, mj+1):
                blank[i][j] += box[k][4]
                if blank[i][j] == 3:
                    cnt += 1

    print(f'#{tc+1} {cnt}')



