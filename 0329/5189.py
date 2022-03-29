# [1][2] - [2][3] - [3][4] - [4][3] - [3][2] - [2][1]
# [1][3] - [3][4] - [4][2] - [2][3] - [3][1]
def f(n, i, j, s):  #n 배열크기 i j 시작 행열, s 시작 값



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

