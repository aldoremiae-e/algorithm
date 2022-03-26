T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())

    lst = [0 for _ in range(N)]
    # Q 번 돌릴거고
    for i in range(1, Q+1):
        # L~R번째 원소를 0에서 i로 바꿀거임
        L, R = map(int, input().split())
        for j in range(N):
            if j == L-1:
                while L-1 <= j < R:
                    lst[j] = i
                    j += 1
    print(f'#{tc}', end=' ')
    print(*lst)