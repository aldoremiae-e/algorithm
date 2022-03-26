'''
가장 큰수, 가장 작은수, 2번째 큰수, 두번째 작은수 ...
선택정렬 활용해서, 인덱스를 짝홀수로 나눠서
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    '''for i in range(N): 과 비교했을 때, 우리는 앞에 정렬된 10개만 필요하기 때문에 10으로 하면됨
        굳이 N으로 한다는 것은 메모리 소모
    '''
    for i in range(10):
        max_idx, min_idx = i, i
        if i % 2 == 0:
            for j in range(i+1,N):
                if arr[j] > arr[max_idx]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            for j in range(i+1,N):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # print(f'#{tc}', *arr[:10])
    print(arr)
    print(f'#{tc}', end=' ')
    for k in range(10):
        print(arr[k], end=' ')
    print()




