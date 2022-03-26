T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maxV = 0
    corridor = [0] * 201
    for i in range(N):
        start, end = map(int, input().split())
        if start < end:
            for j in range((start-1)//2, (end-1)//2 + 1):
                corridor[j] += 1
        else:
            for j in range((start-1)//2, (end-1)//2 - 1, -1):
                corridor[j] += 1
        for x in corridor:
            if maxV < x:
                maxV = x
    print(f'#{tc} {maxV}')