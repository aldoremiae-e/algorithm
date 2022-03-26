T = int(input())
for tc in range(1, T+1):
    S, N = map(str, input().split())
    n = int(N)
    arr = list(map(str, input().split()))
    lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    arr2 = [0] * n
    # 리스트의 숫자를 우리체계와 맞도록
    for idx in range(n):
        for jdx in range(10):
            if arr[idx] == lst[jdx]:
                arr2[idx] = jdx

    # 선택정렬
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr2[min_idx] > arr2[j]:
                min_idx = j
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]

    result = [''] * n
    for idx in range(n):
        for jdx in range(10):
            if arr2[idx] == jdx:
                result[idx] = lst[jdx]

    print(f'#{tc}')
    for k in range(n):
        print(result[k], end=' ')


