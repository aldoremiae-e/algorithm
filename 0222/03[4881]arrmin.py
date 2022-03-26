'''
완전탐색 이용
[0, 1, 2]
[0, 2, 1]
[1, 0, 2]
[1, 2, 0]
[2, 1, 0]
[2, 0, 1]  < = index는 행, 값은 그 행의 열
각 행 당 열의 합들의 최솟값을 찾아서 리턴
'''
'''
완전탐색의 방법은?
재귀함수를 이용한다.
p = [0, 1, 2] 의 리스트 아놔 어려어ㅜ왕
'''
def f(i, N, tot): # 행, 배열크기, 부분합
    global minV
    if i == N:
        tot = 0
        for row in range(N):
            tot += arr[row][p[row]]
        if minV > tot:
            minV = tot
    elif minV != 1000 and tot >= minV:
        return minV
    else:
        # 순열
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N, tot + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]
    return minV

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    minV = 1000
    print(f'#{tc} {f(0, N, 0)}')
