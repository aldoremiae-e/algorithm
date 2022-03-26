def f1(i, M, N, K):
    global result
    if i == M:
        s = 0   # 부분집합의 합
        c = 0   #  원소의 개수를 셀 변수
        for j in range(M):
            if bit[j]:
                s += a[j]
                c += 1

        # 부분집합의 원소가 N개이고 그 원소의 합이 K일 때
        if s == K and c == N:
            result += 1

    else:
        bit[i] = 1
        f1(i+1, M, N, K)
        bit[i] = 0
        f1(i+1, M, N, K)
    return 0

T = int(input())
for tc in range(1, T+1):
    # N : 원소의 개수 , K : 원소의 합
    N, K = map(int, input().split())
    a = [x for x in range(1, 13)]
    M = len(a)
    bit = [0] * M
    result = 0
    f1(0, M, N, K)

    print(f'#{tc} {result}')
