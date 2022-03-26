
'''slice 사용하여 문자열 비교'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [str(input()) for _ in range(M)]
    # 가로
    for i in range(N):
        for j in range(N-M+1):  # 가로줄 몇번읽어?
            result = 0
            for k in range(M//2):
                if arr[i][j] == arr[i][-1-j]:
                    result = 1
                else:
                    break
            if result:
                print(f'#{tc} {arr[i]}')


    #세로
    for j in range(M):
        for i in range(M-N+1):  # 세로줄 몇번읽어?
            result = 0
            for k in range(N//2):
                # j번째의 i번째문자와 j번쨰의 -1-i번째 문자
                if arr[i][j] == arr[-1-i][j]:
                    print(arr[i][j], end='')
                else:
                    break


    #print(result2)
    # 불일치가 발생한 앞 부분에 대해 다시 비교하지 않고 매칭 수행

    # 패턴을 전처리하여 next[M]을 구해서 잘못된 시작 최소화
    # next[M] 불일치가 발생했을 경우 이동할 다음 위치

    # 매칭이 실패했을 때 돌아갈 곳을 계산
    # 이 때 돌아갈 곳의 계산 값이 최대값 즉, 같은문자 그다음칸