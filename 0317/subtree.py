def in_order(v):
    global cnt

    if v == 0:
        return
    cnt += 1
    in_order(ch1[v])
    in_order(ch2[v])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E + 1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:     # 자식 노드가 없으면
            ch1[p] = c
        else:       # 자식 노드가 있을 때
            ch2[p] = c

    cnt = 0
    in_order(N)
    print(f'#{tc} {cnt}')