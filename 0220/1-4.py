T = int(input())
for tc in range(1, T+1):
    num = list(map(int, (input())))

    # 카운팅 정렬 이용
    cnt = [0 for _ in range(10)]
    for i in num:
        cnt[i+1] += 1

    # tri
    tri = 0
    for j in range(10):
        if cnt[j] >= 3:
           tri += 1
           cnt[j] -= 3

    # run
    run = 0
    for j in range(8):
        if cnt[j] > 0 and cnt[j+1] > 0 and cnt[j+2] > 0:
            run += 1
            cnt[j] -= 1
            cnt[j+1] -= 1
            cnt[j+2] -= 1

    if tri+run == 2:
        print('baby-gin')
    else:
        print('lose')