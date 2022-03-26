# count 배열
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    cnt = [0] * 10

    for i in range(len(arr)):
        cnt[arr[i]] += 1
    max_num = 0
    max_cnt = cnt[0]
    for i in range(len(cnt)):
        if cnt[i] > max_cnt:
            max_cnt = cnt[i]
            max_num = i
    print(f'#{tc} {} {max_cnt}')