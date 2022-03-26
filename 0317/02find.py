#LVR
def inorder(n):
    global cnt
    if n <= N:
        inorder(n*2)
        # 사이에 진행해야지 인오더
        tree[n] = cnt
        cnt += 1

        inorder(n*2+1)

for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')