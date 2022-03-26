# LRV
def post(n):
    # 아래서부터 올라가야하니까
    if n <= N:
        tree[n] += post(n*2)    # 왼쪽
        tree[n] += post(n*2+1)  # 오른쪽
        return tree[n]
    else: # 트리성립 X
        return 0

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # 노드의 개수, 리프 노드의 개수, 값을 출력할 노드 번호
    # 정점의 개수 = 노드 + 1
    # 인덱스가 부모, 자식을 저장
    tree = [0] * (N+1)
    # M : 리프 노드의 개수
    for _ in range(M):
        idx, c = map(int, input().split())
        tree[idx] = c
    print(f'#{tc} {post(L)}')