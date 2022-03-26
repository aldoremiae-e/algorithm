T=10
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 5 8 3 1 5 6 9 9 3 2 2 4

    # 버블정렬
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    #카운트정렬
    cnt_lst = [0]*101
    for i in range(len(arr)):
        cnt_lst[arr[i]] += 1
    min_num = 0
    max_num = 0
    check = 0

    for i in range(100):
        my_sum = 0
        if cnt_lst[i] == 0:
            if check == 0:
                continue
        for j in range(0, i + 1):
            my_sum = my_sum + cnt_lst[j] * (i - j + 1)
        if my_sum > N:
            min_num = i
            break
        else:
            check = 1
            continue
        
    check = 0

    for i in range(100, -1, -1):
        my_sum = 0
        if cnt_lst[i] == 0:
            if check == 0:
                continue
        for j in range(100, i - 1, -1):
            my_sum = my_sum + cnt_lst[j] * (j - i + 1)
        if my_sum > N:
            max_num = i
            break
        else:
            check = 1
            continue
    print(f'#{tc} {max_num-min_num}')
