T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input())) # input을 어떻게 받는지가 중요

    # count 배열을 활용해 Greedy 사용
    cnt = [0] * 10
    for i in range(6):
        cnt[num[i]] += 1

    i = 0
    tri = run = 0
    while i < 10:
        if cnt[i] >= 3: # tri 조사
            cnt[i] -= 3
            tri += 1
            continue
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1: # run 조사
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            run += 1
            continue
        i += 1
    if tri + run == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
