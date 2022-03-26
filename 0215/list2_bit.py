'''
N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수 출력
'''

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    result = 0
    for i in range(1 << 12):    # 1<<n :총 부분집합의 개수
        cnt = 0                 # 부분집합의 개수
        total = 0               # 부분집합의 합
        for j in range(12):     # 원소의 수만큼 비트를 비교함
            if i & (1 << j):    # i의 j번째 비트가 1일 경우
                cnt += 1        # 부분집합의 개수 늘리고
                total += j+1 # 부분집합의 합은 j+1

        if cnt == N and total == K:
            result += 1

    print(f'#{tc} {result}')