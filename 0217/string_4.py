'''  Brute Force '''
# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    pat = str(input())
    txt = str(input())
    M = len(pat)
    N = len(txt)

    i = 0 # txt의 인덱스
    j = 0 # pat의 인덱스
    # i랑 j가 점점 옆으로 갈거임
    while i < N and j < M:
        # 만약 txt 첫번째랑 pat 첫번쨰랑 다르면
        if txt[i] != pat[j]:
            # i 이전 시작 다음으로, j 맨앞으로
            i = i -j
            j = -1
        # 점점 옆으로 갈거임
        i += 1
        j += 1
    # while 문을 빠져나왔는데 j가 M까지 갔다면 일치하는게 있는 것
    if j == M:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
