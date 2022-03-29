def play1(cnt):
    for i in range(10):
        if cnt[i] >= 3:
            return 1
    for i in range(8):
        if cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:  # run 조사
            return 1
    return 0

def play2(cnt):
    for i in range(10):
        if cnt[i] >= 3:
            return 2
    for i in range(8):
        if cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:  # run 조사
            return 2
    return 0

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

    cnt1 = [0] * 10
    cnt2 = [0] * 10
    ans = 0
    for i in range(N):
        if ans != 0 : break
        if i % 2:
            cnt2[arr[i]] += 1
            ans = play2(cnt2)
        else:
            cnt1[arr[i]] += 1
            ans = play1(cnt1)
    print(f'#{tc} {ans}')