T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())     #버스 노선 수
    arr = [list(map(int, input().split())) for _ in range(N)]  #arr[i][0] 부터 arr[i][1]까지 해야하니까
    P = int(input())     #버스 정류장 수
    num = [int(input()) for _ in range(P)]     # 지나야하는 버스 정류장


    cnt = [0] * 5001
    for i in range(N):
        for k in range(arr[i][0], arr[i][1]+1):
            cnt[k] += 1
    result = []
    for x in range(P):
        result.append(cnt[num[x]])
    print(*result)

