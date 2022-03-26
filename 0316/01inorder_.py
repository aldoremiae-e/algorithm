def inorder(n):
    if n <= N: # 8
        inorder(n*2)
        print(txt[n-1], end='')
        inorder(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    txt = []

    for i in range(1, N+1): #8
        lst = list(map(str, input().split()))
        txt.append(lst[1])
    print(f'#{tc}',end=' ')
    inorder(1)