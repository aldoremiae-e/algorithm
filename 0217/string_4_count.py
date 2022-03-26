T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str2)
    M = len(str1)

    # count 정렬이용?
    cnt = [0 for _ in range(M)]

    # str2 에서 str1가 있으면 count 해버려
    for i in range(N):
        for j in range(M):
            if str2[i] == str1[j]:
                cnt[j] += 1
    maxV = 0
    for k in range(M):
        if cnt[k] > maxV:
            maxV = cnt[k]
    print(f'#{tc} {maxV}')