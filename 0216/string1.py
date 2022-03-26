'''
연속된 1의 개수의 최댓값
'''
T = int(input())
for tc in range(1,T+1):
    # 어떻게 입력값을 받을까?
    N = int(input())
    # 붙어들어오면 input() 띄어들어오면 input().split()
    arr = list(map(int, input()))
    # 훑었을 때 1을 만나면 cnt 를 저장하도록 하고 0을 다시 만나면 0이 되야겠다.
    maxV = 0
    for i in range(N):
        if arr[i] == 0:
            cnt = 0
        if arr[i] == 1:
            cnt += 1
        # maxV 로 cnt를 비교해서 가장 큰 값을 찾도록
            if cnt > maxV:
                maxV = cnt
    print(f'#{tc} {maxV}')



