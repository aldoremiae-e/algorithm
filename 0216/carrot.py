'''
자기 자신과 비교하는 방법
'''
# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # 당근의 개수
    N = int(input())
    arr = list(map(int, input().split()))
    # 연속이 몇번 되는지
    cnt = 1
    # 최대 연속이 몇번인지
    maxV = 1
    # 1부터 시작하여 전꺼를 같이
    for i in range(1, N):
        # 만약 전꺼가 지금꺼보다 작다면
        if arr[i-1] < arr[i]:
            # 연속 +1
            cnt += 1
            # 만약 최대 수가 바뀐다면
            if cnt > maxV:
                maxV = cnt
        # 아니라면 초기화
        else:
            cnt = 1
    print(f'#{tc} {maxV}')
