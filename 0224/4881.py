# 자리바꿔서 순열찾기
def f(i, N):
    global minV
    if i == N:
        # print(p) 순열 잘 만들어졌나 확인
        # 내가지금 선택한 원소들의 합
        tot = 0
        for j in range(N):
            tot += arr[j][p[j]]
        if minV > tot:
            minV = tot

    else:
        # 모든 행에서 열 선택하기
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]
    return minV

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [x for x in range(N)]

    minV = 1000
    print(f(0, N))