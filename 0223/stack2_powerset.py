'''
집합 {1,2,3}의 원소에 대해 각 부분집합에서의 포함 여부를 트리로 표현
'''

def f(i, N, K): # i 부분집합에 포함될지 결정할 원소의 인덱스, N: 전체 원소개수 K: 찾는 합
    global cnt
    cnt += 1
    if i == N:  # 한개의 부분집합 완성
       #print(bit, end=' ')
        s = 0   # 부분집합 원소의 합
        for j in range(N):
            if bit[j]:
                s += a[j]   # bit[j]가 1이면 a[j]가 부분집합에 포함
        if s == K:          # 부분집합의 합이 K와 같을 떄
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')
            print()
    else:
        # 가지치기
        bit[i] = 1 # 1을 넣는 경우
        f(i+1, N, K)
        bit[i] = 0 # 0을 넣는 경우
        f(i+1, N, K)


a = [x for x in range(1, 11)]
N = len(a)
bit = [0] * N
K = 10
cnt = 0
f(0, N, K)
print(cnt)