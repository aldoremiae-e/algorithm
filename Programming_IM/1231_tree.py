def in_order(n): #LVR
    if n <= N:
        in_order(2*n)  # L
        print(tree[n], end='')  # V
        in_order(2*n+1)     # R

T = 1
for tc in range(1, T+1):
    N = int(input())
    tree = [''] * (N+1)

    for i in range(N):
        arr = list(map(str, input().split()))
        tree[int(arr[0])] = arr[1]
    print(f'#{tc} ', end='')
    in_order(1)