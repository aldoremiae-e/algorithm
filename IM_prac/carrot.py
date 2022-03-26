T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    diff = []
    a = 0     # 일꾼1, 일꾼2 당근수
    for i in range(N):
        a += arr[i]
        b = 0
        for j in range(i+1, N):
            b += arr[j]
        diff.append(abs(a-b))

    min_v = 0
    for k in range(N):
        if diff[k] < diff[min_v]:
            min_v = k
    print(f'#{tc} {min_v+1} {diff[min_v]}')
