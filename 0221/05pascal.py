'''
파스칼 스택이용해서 쓰려면?
dp
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1]*(i+1) for i in range(N)]

    for i in range(len(arr)):
        if i >= 2:
            for j in range(i):
                if j == 0 or j == i:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{tc}')
    for x in arr:
        print(*x)
