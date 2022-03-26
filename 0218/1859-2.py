#뒤로부터 시작! 시간복잡도 N

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    sol = 0
    maxV = lst[-1]
    for i in range(N-2,-1,-1):
        if maxV < lst[i]:
            maxV = lst[i]
        else:
            sol += (maxV - lst[i])
    print(f'#{tc} {sol}')