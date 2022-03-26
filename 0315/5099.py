T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    rear = N
    front = 0
    q = [0] * N     # 화덕
    idx = [0] * N
    # 초기 화덕에 피자를 채워넣음
    for i in range(N):
        q[i] = cheese[i]
        idx[i] = i
    while sum(q) != 0:  # 화덕에 피자가 없을 때
        check = front % N # 인덱스
        # 치즈 반갈
        q[check] = q[check] // 2
        if q[check] == 0:
            if rear < M:    # 다음피자가 존재할 때
                idx[check] = rear   # 화덕에 피자변경
                q[check] = cheese[rear]
                rear += 1
            else:
                q[check] = 0
        front += 1


    # while문을 빠져나올 떄 마지막으로 본 화덕 인덱스 : check
    # 화덕에 있던 피자의 인덱스
    print(f'#{tc} {idx[check]+1}')
