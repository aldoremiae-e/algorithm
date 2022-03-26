''' 가장 긴 회문을 구한다 '''

# 일단 회문이 있는지 확인
# 몇개짜리 회문인지 어떻게 암?


for T in range(10):
    tc = int(input())
    # 글자판은 100*100
    arr = [input() for _ in range(100)]
    N, M = 100, 100
    x = True
    max_v = 0
    # 왜 트루......
    while x is True:
        # 가로
        for i in range(N):
            for j in range(N-M+1):
                check = 0
                for k in range(M//2):
                    if arr[i][j+k] != arr[i][j+M-1-k]:
                        break
                    else:
                        check += 1
                if check == M//2:
                    max_v = M
                    x = False
        # 세로
        for i in range(N):
            for j in range(N-M+1):
                check = 0
                for k in range(M//2):
                    if arr[j+k][i] != arr[j+M-1-k][i]:
                        break
                    else:
                        check += 1
                if check == M//2:
                    max_v = M
                    x = False
        M -= 1

    print(f'#{tc} {max_v}')