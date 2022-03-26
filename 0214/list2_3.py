T = int(input())
for tc in range(1,T+1):
    N = 10
    arr = list(map(int, input().split()))

    for i in range(1, 1<<N): #공집합 제외
        s = 0
        for j in range(0, N):
            if (i & (1<<j)):
                s += arr[j]
        if s == 0: # 0이 한번이라도 되면
            print(f'#{tc} 1')
            break
    else: # 다 돌았는데 없으면
        print(f'#{tc} 0')