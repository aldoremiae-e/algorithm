T = int(input())
for tc in range(1, T+1):
    cnt = [0] * 1001
    N = int(input())
    for _ in range(N):
        K, A, B = map(int, input().split())
        if K == 1:      #일반 , 모든 정류장 정지
            for i in range(A, B+1):
                cnt[i] += 1
        elif K == 2:    #급행 A짝수 - 짝수만, 홀수 - 홀수만, B정지
            cnt[B] += 1
            for i in range(A, B, 2):
                cnt[i] += 1

        else:           #A , B는 따로 처리
            cnt[A] += 1
            cnt[B] += 1
            for i in range(A+1,B):
                if A % 2 == 1 and i % 3 == 0 and i % 10 != 0:    #3의배수, 10의 배수 X
                    cnt[i] += 1
                elif A % 2 == 0 and i % 4 == 0:
                    cnt[i] += 1
    maxV = 0
    for i in range(1, 1001):
        if maxV < cnt[i]:
            maxV = cnt[i]
    print(f'#{tc} {maxV}')