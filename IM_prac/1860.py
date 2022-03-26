'''
M의 배수마다 K개 더해진다.
for문을 쓰는건 너무 어려워.
'''

T = int(input())
for tc in range(1, T+1):
    # N 사람수 M 시간 K 붕어빵 개수
    N, M, K = map(int, input().split())
    # 사람이 도착할 시간
    person = list(map(int, input().split()))


    for i in range(0,N*M,M):

