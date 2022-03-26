T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    #  arr 원소 하나씩
    res = 0
    cnt = arr[0]
    long = [arr[0]]
    max_num = 0

    for i in range(1, len(arr)):
        # 전거랑 앞에랑 비교해서 크면,
        if arr[i-1] < arr[i]:
            cnt += arr[i]

            if max_num < cnt:
                max_num = cnt

        else:
            cnt = arr[i]
            long = [arr[i]]
            if max_num < cnt:
                max_num = cnt

        long.append(arr[i])
        print(long)