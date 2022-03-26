# 어디에 단어가 들어갈 수 있을까?
def count_arr(N):
    ret = 0
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ret += 1
                cnt = 0
    return ret
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0]*(N+1))
    sol = count_arr(N)
    # zip함수란 쉽게말해서 2차원배열을 세로로 읽어오는 느낌
    arr = list(map(list, zip(*arr)))
    sol += count_arr(N)
    print(f'#{tc} {sol}')
