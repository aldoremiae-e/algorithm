T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    charger = [0] + lst + [N]   # N : 종점번호
    cnt = 0
    last = 0                   # last : 마지막 충전위치
    for i in range(1, M+2):     # 도착확인할 정류장 인덱스
        if charger[i] - charger[i-1] > K:
            cnt = 0
            break;
        elif charger[i] - last > K: # 마지막 충전위치로부터 다음 위치까지 갈 수 없니
            last = charger[i-1]
            cnt += 1
    print(f'#{tc} {cnt}')
