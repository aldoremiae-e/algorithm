T = int(input())
for tc in range(1, T+1):
    lst = input()
    cnt = 0
    sol = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            cnt += 1
        else:
            # 레이저
            if lst[i-1] == '(':
                cnt -= 1
                sol += cnt
            # 쇠막대기 감소
            else:
                cnt -= 1
                sol += 1

    print(f'#{tc} {sol}')