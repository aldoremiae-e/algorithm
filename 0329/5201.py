T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    #컨테이너 수, 트럭 수
    W = list(map(int, input().split()))   #컨테이너 당 화물의 무게
    T = list(map(int, input().split()))  #트럭 당 적재용량

    # 정렬 - 내림차순으로 정렬했기 때문에, 큰 것부터 넣어서 최댓값 넣어짐
    W.sort(reverse=True)
    T.sort(reverse=True)

    # 가능한 화물 넣기
    w, t = 0, 0
    ans = 0
    while w < N and t < M:  # 완전탐색?
        if W[w] <= T[t]:    # 화물무게 <= 적재용량
           ans += W[w]
           w += 1
           t += 1
        else:               # 화물무게 > 적재용량
            w += 1
    print(f'#{tc} {ans}')