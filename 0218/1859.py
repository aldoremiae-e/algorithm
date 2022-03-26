#시간복잡도 N^2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    start = 0
    sol = 0
    while start < N:
        maxV = start
        # max 값 찾기
        for i in range(start, N):
            if lst[maxV] < lst[i]:
                maxV = i
        # max index까지 차이를 더해줘
        for j in range(start, maxV):
            sol += lst[maxV] - lst[j]
        # start값 max 다음
        start = maxV + 1
    print(f'#{tc} {sol}')