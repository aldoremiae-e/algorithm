# 순열
def nPr(n, k, m):  #j 인덱스 설정
    if n == (k-1):
        print(p)
    else:
        for i in range(m):
            if v[i] == 0:
                v[i] = 1
                p[i] = a[i]
                nPr(n+1, k, m)
                v[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    a = [i for i in range(N)]
    p = [0] * N
    v = [0] * N
    sol = 99999
    nPr(0, N, N)
