def f(N):
    s = 0
    e = 10000000
    while s <= e:
        i = (s + e) // 2
        if arr[i] == N:
            return i
        elif arr[i] < N:    # 제곱근보다 작으면
            s += 1
        else:
            e -= 1      #제곱근보다 크면
    return -1

T = int(input())
arr = [x**3 for x in range(10000001)]
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {f(N)}')

